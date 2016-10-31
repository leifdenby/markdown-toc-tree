# Quick table of contents for markdown in console

To use this script simple pipe all the markdown/pandoc files to it that are
part of your document:

>   cat thesis/\*/\*.md | python -m mdtoctree

And you get a useful table of contents printed out:

```
. 
├── 1. Introduction
├── 2. Background
│   ├── 21. Atmospheric conditions for moist convection
│   ├── 22. The importance of entrainment
│   └── 23. Approaches to convective parameterisation
│       └── 231. Convective Cloud Field Model (CCFM)
├── 3. 1D Cloud-model
│   ├── 31. Cloud-model equations
│   │   ├── 311. Conservation of mass
│   │   ├── 312. Conservation of momentum
│   │   ├── 313. Conservation of energy
│   │   ├── 314. Tracer equations
│   │   └── 315. Summary of cloud-model equations
│   ├── 32. Boundary and initial conditions
│   │   └── 321. Cloud-base conditions
│   ├── 33. Model integration algorithm
│   └── 34. Properties of convective clouds inferred from entraining-parcel model
│       ├── 341. Effect of drag on cloud-evolution
│       ├── 342. Entrainment vs drag
│       ├── 343. Effect of entrainment on cloud-evolution
│       ├── 344. Sensitivity of cloud-profiles to rain-out rate
│       └── 345. Boundary-layer perturbations and predicted cloud-profiles
├── 4. Cloud microphysics
│   ├── 41. Microphysics processes
│   │   ├── 411. Droplet formation and growth model
...
```

Pull requests welcome!
