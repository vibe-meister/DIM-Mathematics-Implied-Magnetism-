# Field Measurement Protocols for Tesla Coils

## 1. Electric Field Measurements

### High-Voltage Probes
- **Type**: Resistive divider probes
- **Range**: 0-100 kV
- **Bandwidth**: DC to 1 MHz
- **Accuracy**: ±1%

### Measurement Setup
```
V_measured = V_probe × (R1 + R2)/R2
```

### Safety Considerations
- Use appropriate PPE
- Maintain safe distances
- Use insulated tools
- Follow lockout/tagout procedures

## 2. Magnetic Field Measurements

### Hall Effect Probes
- **Type**: Linear Hall sensors
- **Range**: 0-10 T
- **Bandwidth**: DC to 100 kHz
- **Accuracy**: ±0.1%

### Rogowski Coils
- **Type**: Air-core current transformers
- **Range**: 0-1000 A
- **Bandwidth**: 1 Hz to 1 MHz
- **Accuracy**: ±0.5%

### Measurement Setup
```
B = (μ₀I)/(2πr) [for straight wire]
I = (1/μ₀)∫B·dl [for closed loop]
```

## 3. Frequency Domain Analysis

### Network Analyzer
- **Type**: Vector network analyzer (VNA)
- **Range**: 1 MHz to 6 GHz
- **Accuracy**: ±0.1 dB
- **Phase accuracy**: ±0.1°

### Impedance Measurements
```
Z = V/I = R + jX
|Z| = √(R² + X²)
φ = arctan(X/R)
```

### S-Parameter Measurements
```
S11 = (b1/a1)|a2=0 [reflection coefficient]
S21 = (b2/a1)|a2=0 [transmission coefficient]
```

## 4. Time Domain Analysis

### Oscilloscope
- **Type**: Digital storage oscilloscope
- **Bandwidth**: 1 GHz
- **Sample rate**: 10 GS/s
- **Memory**: 1 M points

### Signal Processing
- **FFT**: Frequency domain analysis
- **Windowing**: Reduce spectral leakage
- **Averaging**: Improve signal-to-noise ratio

### Triggering
- **Level trigger**: Voltage threshold
- **Edge trigger**: Rising/falling edge
- **Pulse trigger**: Pulse width/duty cycle

## 5. Power Measurements

### RF Power Meter
- **Type**: Thermocouple or diode detector
- **Range**: 1 mW to 100 W
- **Frequency**: 1 MHz to 6 GHz
- **Accuracy**: ±5%

### Power Calculation
```
P = V²/R = I²R
P_avg = (1/T)∫P(t)dt
```

### Efficiency Measurement
```
η = P_out/P_in × 100%
```

## 6. Resonance Analysis

### Frequency Sweep
- **Method**: Continuous frequency sweep
- **Range**: 100 kHz to 10 MHz
- **Resolution**: 1 kHz
- **Dwell time**: 100 ms

### Q Factor Measurement
```
Q = f₀/Δf
Δf = f₂ - f₁ [at -3 dB points]
```

### Bandwidth Measurement
```
BW = f₂ - f₁
BW = f₀/Q
```

## 7. Coupling Measurements

### Mutual Inductance
```
M = k√(L₁L₂)
k = M/√(L₁L₂)
```

### Measurement Method
1. Measure L₁ and L₂ separately
2. Measure L_total with coils coupled
3. Calculate M = (L_total - L₁ - L₂)/2

### Coupling Coefficient
```
k = M/√(L₁L₂)
```

## 8. Field Mapping

### 3D Field Mapping
- **Grid**: 10×10×10 points
- **Resolution**: 1 cm
- **Measurement time**: 1 hour
- **Data format**: CSV or HDF5

### Automated Scanning
- **Motor control**: 3-axis positioning
- **Data acquisition**: Real-time measurement
- **Synchronization**: Triggered measurements

### Data Processing
- **Interpolation**: Smooth field surfaces
- **Visualization**: 3D field plots
- **Analysis**: Field gradients and patterns

## 9. Calibration Procedures

### Probe Calibration
1. Use known reference fields
2. Apply calibration factors
3. Verify linearity
4. Document calibration date

### System Calibration
1. Check all connections
2. Verify measurement ranges
3. Test with known signals
4. Record calibration results

### Traceability
- **Standards**: NIST traceable
- **Documentation**: Calibration certificates
- **Frequency**: Annual calibration
- **Records**: Maintain calibration history

## 10. Data Analysis and Reporting

### Statistical Analysis
- **Mean**: Average field values
- **Standard deviation**: Measurement uncertainty
- **Confidence intervals**: 95% confidence level
- **Outliers**: Identify and investigate

### Uncertainty Analysis
```
u_total = √(u₁² + u₂² + ... + uₙ²)
```

### Reporting Format
- **Executive summary**: Key findings
- **Methodology**: Measurement procedures
- **Results**: Data tables and plots
- **Conclusions**: Analysis and recommendations

### Data Archival
- **Format**: CSV, HDF5, or database
- **Metadata**: Measurement conditions
- **Backup**: Multiple copies
- **Retention**: 7 years minimum
