def add_adduct(spectrum_in):
    """Add adduct to metadata (if not present yet).

    Method to interpret the given compound name to find the adduct.
    """

    spectrum = spectrum_in.clone()

    if 'adduct' not in spectrum.metadata:
        try:
            name = spectrum.metadata["name"]
            adduct = name.split(' ')[-1]
            adduct = adduct.replace('\n', '') \
                           .replace(' ', '')  \
                           .replace('[', '')  \
                           .replace(']', '')  \
                           .replace('*', '')
            if adduct:
                spectrum.metadata["adduct"] = adduct
        except KeyError:
            print("Spectrum's metadata does not have a 'name'.")

    return spectrum
