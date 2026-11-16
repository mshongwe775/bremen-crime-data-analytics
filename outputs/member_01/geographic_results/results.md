# Data preparation and district analysis
Original author: Meriam El Askri.

The frozen preparation retains all 5,126 source IDs, original texts, URLs and both supplied embeddings. BR001569 and BR002114 are excluded duplicates, leaving 5,124 eligible reports. The frozen Parquet file is never overwritten.

Both geographic views and original mapping evidence are preserved in Notebook 01 metadata. The Ortsteil view locates 2,977 reports and retains 2,147 Unknown; the broader view locates 4,149 and retains 975 Unknown. The views overlap and must not be added. Four protected report-level exceptions remain Unknown.

`geographic_results/` contains category counts, district totals, shares, leaders, geographic coverage and source-label evidence. Five figures show counts, composition and coverage. Categories use the retained computational mapping directly. Counts describe publications, not confirmed crimes or risk rates. Compatible boundaries, population exposure and collection completeness are unavailable.

Among named broader areas, Walle leads Traffic-related (85), Mitte leads Assault / threats (117) and Drug-related (62), and Neustadt leads Robbery (33) and Fire / explosion / ordnance (52). Category denominators include Unknown geography; zero directly mapped Theft/Weapons cases do not imply absence.
