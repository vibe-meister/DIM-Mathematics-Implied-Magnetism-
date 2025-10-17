# Tesla Coil Geometry Analysis Using Maxwell's Equations

## 1. Cylindrical Coordinate System Setup

### Coordinate System
- r: radial distance from coil axis
- φ: azimuthal angle
- z: axial position along coil

### Field Components
```
E = E_r(r,φ,z)r̂ + E_φ(r,φ,z)φ̂ + E_z(r,φ,z)ẑ
B = B_r(r,φ,z)r̂ + B_φ(r,φ,z)φ̂ + B_z(r,φ,z)ẑ
```

## 2. Primary Coil Analysis

### Current Distribution
- N₁ turns, radius R₁, height h₁
- Current: I₁(t) = I₀sin(ωt)

### Magnetic Field (Solenoid Approximation)
```
B_z = μ₀N₁I₁/h₁ [inside coil]
B_r = 0 [inside coil]
B_φ = 0 [inside coil]
```

### Electric Field (from ∂B/∂t)
```
E_φ = -(r/2)(∂B_z/∂t) = -(r/2)μ₀N₁(∂I₁/∂t)/h₁
```

## 3. Secondary Coil Analysis

### Induced Current
```
I₂ = -(M/L₂)(dI₁/dt)
```

### Self-Inductance (Wheeler's Formula)
```
L₂ = (μ₀N₂²πR₂²)/h₂ × [1 + 0.9(R₂/h₂)]
```

### Mutual Inductance
```
M = k√(L₁L₂)
```

## 4. Field Coupling Analysis

### Coupling Coefficient Calculation
```
k = M/√(L₁L₂)
```

### For Coaxial Coils
```
k ≈ (R₁R₂)^(3/2) / [d² + (R₁+R₂)²]^(3/4)
```

Where d is the separation distance.

## 5. Top Load Analysis

### Capacitance to Ground
```
C_top = 4πε₀R_top [sphere approximation]
```

### Electric Field Distribution
```
E = (Q_top)/(4πε₀r²)r̂
```

### Energy Storage
```
U = (1/2)C_topV²
```

## 6. Resonant Mode Analysis

### Fundamental Mode
```
f₀ = 1/(2π√(L₂C_total))
```

### Higher Order Modes
```
f_n = nf₀ [for n = 1, 2, 3, ...]
```

### Mode Shapes
- Fundamental: λ/4 standing wave
- Second harmonic: λ/2 standing wave
- Third harmonic: 3λ/4 standing wave

## 7. Field Visualization Parameters

### Stream Function for Magnetic Field
```
ψ = (1/2)μ₀I₁r² [for primary]
```

### Potential Function for Electric Field
```
φ = V_top - ∫E·dl
```

### Field Line Equations
```
dr/B_r = rdφ/B_φ = dz/B_z
```
