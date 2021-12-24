import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import rdDepictor
from rdkit.Chem import rdFMCS
from rdkit.Chem import TemplateAlign

import click

rdDepictor.SetPreferCoordGen(True)

@click.command()
@click.option("--output", "-o", type=str, default="./data", help="Save dir path")
@click.option("--name", "-n", type=str, default="MolToGridImage", help="File name")
@click.option("--align", type=bool, default=True, help="Template align")

def cmd(output, name, align):
    """[summary]

    Args:
        output ([str]): [Save output directory path]
        name ([str]): [output file name]
        align ([bool]): [Aligned display]
    """
    print("RDKit version : ", rdkit.__version__)
    sildenafil = Chem.MolFromSmiles(
        "CCCC1=NN(C)C2=C1NC(=NC2=O)C1=C(OCC)C=CC(=C1)S(=O)(=O)N1CCN(C)CC1"
    )
    vardenafil = Chem.MolFromSmiles(
        "CCCC1=NC(C)=C2N1NC(=NC2=O)C1=C(OCC)C=CC(=C1)S(=O)(=O)N1CCN(CC)CC1"
    )
    if align:
        rdDepictor.Compute2DCoords(sildenafil)
        rdDepictor.Compute2DCoords(vardenafil)
        res = rdFMCS.FindMCS(
            [sildenafil, vardenafil],
            completeRingsOnly=True,
            atomCompare=rdFMCS.AtomCompare.CompareAny,
        )
        MCS = Chem.MolFromSmarts(res.smartsString)
        rdDepictor.Compute2DCoords(MCS)

        TemplateAlign.AlignMolToTemplate2D(sildenafil, MCS)
        TemplateAlign.AlignMolToTemplate2D(vardenafil, MCS)
    img = Draw.MolsToGridImage(
        [sildenafil, vardenafil],
        legends=["sildenafil", "vardenafil"],
        molsPerRow=2,
        subImgSize=(200, 200),
    )
    img.save("{}/{}.png".format(output, name))


def main():
    cmd()


if __name__ == "__main__":
    main()
