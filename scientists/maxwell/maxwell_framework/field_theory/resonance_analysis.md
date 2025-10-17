# Resonance Analysis Using Maxwell's Equations

## 1. Resonant Circuit Fundamentals

### From Ampère-Maxwell Law
```
∇ × B = μ₀J + μ₀ε₀(∂E/∂t)
```

### For Resonant LC Circuit
- L: coil inductance
- C: distributed capacitance
- R: resistance (losses)

### Circuit Equation
```
L(d²I/dt²) + R(dI/dt) + I/C = 0
```

## 2. Natural Resonant Frequency

### Undamped Frequency
```
ω₀ = 1/√(LC)
f₀ = 1/(2π√(LC))
```

### Damped Frequency
```
ω_d = √(ω₀² - (R/2L)²)
```

### Damping Ratio
```
ζ = R/(2√(L/C))
```

## 3. Quality Factor Analysis

### Definition
```
Q = ω₀L/R = 1/(ω₀CR) = √(L/C)/R
```

### Energy Interpretation
```
Q = 2π × (stored energy)/(energy lost per cycle)
```

### Bandwidth Relationship
```
Δf = f₀/Q
```

## 4. Coupled Resonant Systems

### Two-Coupled Oscillators
- Primary: L₁, C₁, R₁
- Secondary: L₂, C₂, R₂
- Mutual inductance: M

### Coupling Coefficient
```
k = M/√(L₁L₂)
```

### Normal Mode Frequencies
```
ω₁² = (1/2)[ω₁₀² + ω₂₀² - √((ω₁₀² - ω₂₀²)² + 4k²ω₁₀²ω₂₀²)]
ω₂² = (1/2)[ω₁₀² + ω₂₀² + √((ω₁₀² - ω₂₀²)² + 4k²ω₁₀²ω₂₀²)]
```

Where:
- ω₁₀ = 1/√(L₁C₁)
- ω₂₀ = 1/√(L₂C₂)

## 5. Tesla Coil Specific Resonance

### Secondary Coil Resonance
```
f_secondary = 1/(2π√(L₂C_distributed))
```

### Distributed Capacitance
```
C_distributed = C_self + C_top + C_ground
```

### Self-Capacitance (Medhurst's Formula)
```
C_self = (2πε₀h)/ln(2h/r_wire)
```

## 6. Field Resonance Modes

### Standing Wave Analysis
```
E(z,t) = E₀sin(nπz/h)cos(ω_nt + φ)
```

### Mode Frequencies
```
f_n = (nc)/(2h) = nf₁
```

Where:
- n = 1, 2, 3, ... (mode number)
- c = speed of light
- h = coil height

## 7. Impedance Analysis

### Input Impedance
```
Z_in = R + j(ωL - 1/(ωC))
```

### At Resonance
```
Z_in = R (purely resistive)
```

### Off-Resonance
```
Z_in = R + jX
X = ωL - 1/(ωC)
```

## 8. Power Transfer Analysis

### Maximum Power Transfer
```
P_max = V²/(4R) [when Z_source = Z_load*]
```

### Efficiency
```
η = P_out/P_in = R_load/(R_source + R_load)
```

## 9. Frequency Response

### Transfer Function
```
H(jω) = V_out/V_in = 1/(1 + jQ(ω/ω₀ - ω₀/ω))
```

### Magnitude Response
```
|H(jω)| = 1/√(1 + Q²(ω/ω₀ - ω₀/ω)²)
```

### Phase Response
```
φ(ω) = -arctan(Q(ω/ω₀ - ω₀/ω))
```
