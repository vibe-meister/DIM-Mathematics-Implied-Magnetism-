# Maxwell Equation Derivations for Tesla Coils

## 1. Primary-Secondary Coupling Analysis

### Starting from Faraday's Law
```
∇ × E = -∂B/∂t
```

### For Tesla Coil Geometry
- Primary coil: radius R₁, N₁ turns, current I₁(t)
- Secondary coil: radius R₂, N₂ turns, mutual inductance M

### Magnetic Field from Primary
```
B₁ = (μ₀N₁I₁)/(2R₁) [for solenoid approximation]
```

### Induced EMF in Secondary
```
ε₂ = -N₂(dΦ₂/dt) = -N₂(d/dt)(M·I₁)
ε₂ = -M(dI₁/dt)
```

### Coupling Coefficient
```
k = M/√(L₁L₂)
```

## 2. Resonant Frequency Analysis

### From Ampère-Maxwell Law
```
∇ × B = μ₀J + μ₀ε₀(∂E/∂t)
```

### For Resonant Circuit
- L: coil inductance
- C: distributed capacitance
- R: resistance

### Resonant Frequency
```
ω₀ = 1/√(LC)
f₀ = 1/(2π√(LC))
```

### Quality Factor
```
Q = ω₀L/R = 1/(ω₀CR)
```

## 3. Field Distribution in Cylindrical Geometry

### Electric Field in Cylindrical Coordinates
```
E = E_r(r,φ,z)r̂ + E_φ(r,φ,z)φ̂ + E_z(r,φ,z)ẑ
```

### Magnetic Field from Current Distribution
```
B = (μ₀I)/(2πr)φ̂ [for straight wire]
B = (μ₀NI)/(2R)ẑ [for solenoid]
```

## 4. Energy Storage and Transfer

### From Poynting Vector
```
S = (1/μ₀)(E × B)
```

### Energy Density
```
u_e = (1/2)ε₀E²
u_m = (1/2)B²/μ₀
u_total = u_e + u_m
```

### Power Flow
```
P = ∮ S · dA
```

## 5. Boundary Conditions at Coil Surfaces

### Electric Field Boundary Conditions
```
E₁⊥ - E₂⊥ = σ/ε₀
E₁∥ - E₂∥ = 0
```

### Magnetic Field Boundary Conditions
```
B₁⊥ - B₂⊥ = 0
B₁∥/μ₁ - B₂∥/μ₂ = K
```

Where:
- σ: surface charge density
- K: surface current density
- μ₁, μ₂: permeabilities of materials
