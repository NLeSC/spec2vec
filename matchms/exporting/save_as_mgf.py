import pyteomics.mgf as py_mgf


def save_as_mgf(spectrums, filename):
    """Save spectrum(s) as mgf file.

    Args:
    ----
    spectrums: list of Spectrum() objects, Spectrum() object
        Expected input are match.Spectrum.Spectrum() objects.
    filename: str
        Provide filename to save spectrum(s).
    """
    if not isinstance(spectrums, list):
        # Assume that input was single Spectrum
        spectrums = [spectrums]

    # Convert matchms.Spectrum() into dictionaries for pyteomics
    spectrum_dicts = []
    for spectrum in spectrums:
        spectrum_dict = {"m/z array": spectrum.mz,
                         "intensity array": spectrum.intensities,
                         "params": spectrum.metadata}
        spectrum_dicts.append(spectrum_dict)

    py_mgf.write(spectrum_dicts, filename)