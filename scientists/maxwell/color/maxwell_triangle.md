# Maxwell Triangle and Barycentric Chromaticity

## Definition
- Given primaries R, G, B, any additive mixture with nonnegative coefficients plots inside the triangle with vertices at the primaries.
- Normalized coordinates: r = R/(R+G+B), g = G/(R+G+B), b = 1 − r − g.

## Barycentric Representation
- A color with tristimulus (R,G,B) maps to triangle point with areas proportional to R, G, B.
- Straight lines represent linear mixtures.

## Properties
- White point lies inside triangle (for balanced primaries).
- Spectral locus generally outside for physical primaries; imaginary primaries extend gamut.
- Negative coefficients indicate matches requiring primary addition to test field.

## Relation to Later Spaces
- Precursor to CIE chromaticity diagrams (rg, xy).
- Preserves additivity and straight-line mixture paths.

## Practical Construction
- Fix triangle vertices for chosen primaries.
- Plot measured matches after normalizing by sum R+G+B.
- Use for gamut visualization and mixture prediction.
