# 3D Field Mapping for Tesla Coils

## 1. Coordinate System and Field Components

### Cylindrical Coordinates
```
r: radial distance from coil axis
φ: azimuthal angle
z: axial position along coil
```

### Field Vector Components
```
E = E_r(r,φ,z)r̂ + E_φ(r,φ,z)φ̂ + E_z(r,φ,z)ẑ
B = B_r(r,φ,z)r̂ + B_φ(r,φ,z)φ̂ + B_z(r,φ,z)ẑ
```

## 2. Primary Coil Field Distribution

### Magnetic Field (Solenoid Model)
```
B_z(r,z) = (μ₀N₁I₁/2h₁)[(z+h₁/2)/√(r²+(z+h₁/2)²) - (z-h₁/2)/√(r²+(z-h₁/2)²)]
```

### Electric Field (from ∂B/∂t)
```
E_φ(r,z) = -(r/2)(∂B_z/∂t) = -(r/2)μ₀N₁(∂I₁/∂t)/h₁
```

### Field Lines
```
dr/B_r = rdφ/B_φ = dz/B_z
```

## 3. Secondary Coil Field Distribution

### Induced Electric Field
```
E_induced = -(∂A/∂t) - ∇φ
```

### Vector Potential
```
A = (μ₀/4π)∫(J(r')/|r-r'|)dV'
```

### Scalar Potential
```
φ = (1/4πε₀)∫(ρ(r')/|r-r'|)dV'
```

## 4. Top Load Field Distribution

### Electric Field (Sphere Model)
```
E_r = (Q_top)/(4πε₀r²) [outside sphere]
E_r = 0 [inside sphere]
```

### Capacitance to Ground
```
C = 4πε₀R_top
```

### Energy Density
```
u_e = (1/2)ε₀E²
```

## 5. Field Visualization Methods

### Stream Function (Magnetic Field)
```
∇ × (ψẑ) = B
```

### Potential Function (Electric Field)
```
E = -∇φ
```

### Field Line Equations
```
dx/E_x = dy/E_y = dz/E_z
```

## 6. Numerical Field Calculation

### Finite Element Method
```
∇²φ = -ρ/ε₀ [Poisson's equation]
∇²A = -μ₀J [Vector Poisson's equation]
```

### Boundary Conditions
```
φ = V [on conductor surfaces]
∂φ/∂n = 0 [on symmetry planes]
```

## 7. Field Mapping Parameters

### Grid Resolution
```
Δr = R_coil/100
Δφ = 2π/360
Δz = h_coil/100
```

### Field Magnitude
```
|E| = √(E_r² + E_φ² + E_z²)
|B| = √(B_r² + B_φ² + B_z²)
```

### Field Direction
```
θ_E = arctan(E_φ/E_r)
φ_E = arctan(E_z/√(E_r² + E_φ²))
```

## 8. Visualization Output Formats

### Vector Field Plots
- Arrow plots showing field direction and magnitude
- Streamlines for field line visualization
- Contour plots for field magnitude

### 3D Surface Plots
- Field magnitude on coil surfaces
- Potential distribution
- Energy density distribution

### Cross-Sectional Views
- Radial field profiles
- Axial field profiles
- Azimuthal field profiles

## 9. Field Analysis Metrics

### Field Strength
```
E_max = max(|E|)
B_max = max(|B|)
```

### Field Gradient
```
∇E = √((∂E/∂r)² + (1/r)(∂E/∂φ)² + (∂E/∂z)²)
```

### Energy Distribution
```
U_total = ∫∫∫(1/2)(ε₀E² + B²/μ₀)dV
```

## 10. Comparison with Tesla's Observations

### Field Patterns
- Compare calculated patterns with Tesla's descriptions
- Identify resonance modes
- Analyze coupling efficiency

### Energy Concentration
- Locate high-energy regions
- Identify field focusing effects
- Analyze energy transfer mechanisms
