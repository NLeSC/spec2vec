import re
from rdkit import Chem


def convert_smiles_to_inchi(smiles):
    return mol_converter(smiles, "smiles", "inchi")


def convert_inchi_to_smiles(inchi):
    return mol_converter(inchi, "inchi", "smiles")


def convert_inchi_to_inchikey(inchi):
    return mol_converter(inchi, "inchi", "inchikey")


def mol_converter(mol_input, input_type, output_type):
    """Convert molecular representations using rdkit.

    Convert for from smiles or inchi to inchi, smiles, or inchikey.

    Args:
    ----
    mol_input: str
        Input data, inchi or smiles.
    input_type: str
        Define input type: "smiles" for smiles and "inchi" for inchi.
    output_type: str
        Define output type: "smiles", "inchi", or "inchikey".
    """
    input_function = {"inchi": Chem.MolFromInchi,
                      "smiles": Chem.MolFromSmiles}
    output_function = {"inchi": Chem.MolToInchi,
                       "smiles": Chem.MolToSmiles,
                       "inchikey": Chem.MolToInchiKey}

    mol = input_function[input_type](mol_input.strip('"'))
    if mol is None:
        return None

    output = output_function[output_type](mol)
    if output:
        return output
    return None


def is_valid_inchi(inchi):
    """Return True if input string is valid InChI.

    This functions test if string can be read by rdkit as InChI.

    Args:
    ----
    inchi: str
        Input string to test if it has format of InChI.
    """
    # First quick test to avoid excess in-depth testing
    if inchi is None:
        return False
    inchi = inchi.strip('"')
    regexp = r"(InChI=1|1)(S\/|\/)[0-9, A-Z, a-z,\.]{2,}\/(c|h)[0-9]"
    if not re.search(regexp, inchi):
        return False
    # Proper chemical test
    mol = Chem.MolFromInchi(inchi)
    if mol:
        return True
    return False


def is_valid_smiles(smiles):
    """Return True if input string is valid smiles.

    This functions test if string can be read by rdkit as smiles.

    Args:
    ----
    inchi: str
        Input string to test if it can be imported as smiles.
    """
    if smiles is None:
        return False

    regexp = r"^([^J][0-9BCOHNSOPIFKcons@+\-\[\]\(\)\\\/%=#$,.~&!|Si|Se|Br|Mg|Na|Cl|Al]{3,})$"
    if not re.match(regexp, smiles):
        return False

    mol = Chem.MolFromSmiles(smiles)
    if mol:
        return True
    return False


def is_valid_inchikey(inchikey):
    """Return True if string has format of inchikey."""
    if inchikey is None:
        return False

    regexp = r"[A-Z]{14}-[A-Z]{10}-[A-Z]"
    if re.fullmatch(regexp, inchikey):
        return True
    return False
