# Tesla Coil Geometric Configurations

## 1. Standard Tesla Coil Geometry

### Primary Coil
- **Shape**: Flat spiral or helical
- **Radius**: R₁
- **Height**: h₁
- **Turns**: N₁
- **Wire gauge**: AWG specification
- **Pitch**: p₁ = h₁/N₁

### Secondary Coil
- **Shape**: Cylindrical solenoid
- **Radius**: R₂
- **Height**: h₂
- **Turns**: N₂
- **Wire gauge**: AWG specification
- **Pitch**: p₂ = h₂/N₂

### Top Load
- **Shape**: Sphere, torus, or other geometry
- **Radius**: R_top
- **Material**: Conductive (aluminum, copper)

## 2. Geometric Parameters

### Aspect Ratio
```
AR = h₂/R₂
```

### Turn Density
```
n₁ = N₁/h₁ [primary]
n₂ = N₂/h₂ [secondary]
```

### Wire Spacing
```
s₁ = p₁ - d_wire [primary]
s₂ = p₂ - d_wire [secondary]
```

### Fill Factor
```
FF = (N × d_wire)/h
```

## 3. Inductance Calculations

### Primary Inductance (Wheeler's Formula)
```
L₁ = (μ₀N₁²πR₁²)/h₁ × [1 + 0.9(R₁/h₁)]
```

### Secondary Inductance (Wheeler's Formula)
```
L₂ = (μ₀N₂²πR₂²)/h₂ × [1 + 0.9(R₂/h₂)]
```

### Mutual Inductance
```
M = k√(L₁L₂)
```

### Coupling Coefficient
```
k = M/√(L₁L₂)
```

## 4. Capacitance Calculations

### Self-Capacitance (Medhurst's Formula)
```
C_self = (2πε₀h)/ln(2h/r_wire)
```

### Top Load Capacitance
```
C_top = 4πε₀R_top [sphere]
C_top = 2πε₀R_top [torus]
```

### Distributed Capacitance
```
C_distributed = C_self + C_top + C_ground
```

## 5. Resonant Frequency

### Secondary Resonance
```
f_secondary = 1/(2π√(L₂C_distributed))
```

### Primary Resonance
```
f_primary = 1/(2π√(L₁C_primary))
```

### Tuning Condition
```
f_primary = f_secondary [for maximum coupling]
```

## 6. Geometric Optimization

### Maximum Coupling
- Minimize separation distance
- Optimize coil radii ratio
- Align coil centers

### Maximum Q Factor
- Minimize wire resistance
- Optimize turn spacing
- Use high-conductivity materials

### Maximum Voltage
- Maximize secondary height
- Optimize top load geometry
- Minimize corona losses

## 7. Tesla's Original Configurations

### Colorado Springs Coil
- **Primary**: Flat spiral, large diameter
- **Secondary**: Tall, narrow cylinder
- **Top Load**: Large sphere
- **Ground**: Extensive grounding system

### Wardenclyffe Tower
- **Primary**: Large helical coil
- **Secondary**: Very tall cylinder
- **Top Load**: Large dome
- **Ground**: Deep grounding system

## 8. Modern Variations

### Dual Resonant Solid State (DRSSTC)
- **Primary**: Flat spiral
- **Secondary**: Standard cylinder
- **Driver**: Solid state switching
- **Control**: Feedback tuning

### Musical Tesla Coil
- **Primary**: Flat spiral
- **Secondary**: Standard cylinder
- **Modulation**: Audio frequency modulation
- **Output**: Musical arcs

## 9. Scaling Relationships

### Geometric Scaling
```
L ∝ N²R²/h
C ∝ R
f ∝ 1/√(LC) ∝ 1/(N√R)
```

### Power Scaling
```
P ∝ V²/R ∝ f²L²/R
```

### Voltage Scaling
```
V ∝ √(P×R) ∝ f×L
```

## 10. Design Guidelines

### Primary Design
- Use thick wire for low resistance
- Keep turns close together
- Use flat spiral for better coupling

### Secondary Design
- Use thin wire for high inductance
- Maintain uniform spacing
- Use tall, narrow geometry

### Top Load Design
- Use smooth, rounded surfaces
- Maximize surface area
- Minimize sharp edges

### Grounding
- Use extensive ground system
- Minimize ground resistance
- Connect to multiple ground points
