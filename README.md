<div align="center">

# Michael ESSOMBA

### Embedded Systems & Robotics Engineering Student @ ENSIM

**Real-time embedded software · Robotics · Electronics · FPGA/VHDL · System integration**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Michael%20Essomba-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/essomba-michael-84b12643b/)
[![GitHub](https://img.shields.io/badge/GitHub-Mickael235-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Mickael235)
[![Email](https://img.shields.io/badge/Email-ENSIM-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:Michael.Essomba_Jabe.Etu@univ-lemans.fr)
![Location](https://img.shields.io/badge/Le%20Mans-France-2F80ED?style=flat-square)
![English](https://img.shields.io/badge/English-B2-4C8BF5?style=flat-square)

<br>

### 🎯 Seeking a 6-month engineering internship from **March 2027**

</div>

---

## About me

I am an engineering student at **ENSIM – Le Mans University**, specializing in **embedded and real-time systems**.

I enjoy working at the boundary between **software and physical systems**: reading sensors, controlling actuators, designing communication layers, validating behavior on real hardware, and integrating complete systems from the microcontroller up to the supervision interface.

My academic and personal projects currently span:

- **STM32 and PIC16 embedded development**
- **robotics and motion control**
- **FreeRTOS / CAN architectures**
- **FPGA and VHDL**
- **PCB design and electronics**
- **instrumentation and automated measurement**
- **Raspberry Pi supervision**
- **ROS2 simulation and digital twins**
- **system testing, debugging and technical documentation**

What I value most in engineering is not only making a feature work, but understanding **why it works, how it fails, how it can be measured, and how it can be improved**.

---

## Engineering profile

<table>
<tr>
<td width="33%" valign="top">

### ⚙️ Embedded systems

- C
- STM32
- PIC16
- GPIO / ADC / PWM / UART
- Interrupt-driven design
- State machines
- FreeRTOS *(current project)*
- CAN *(current project)*

</td>
<td width="33%" valign="top">

### 🤖 Robotics & control

- Mecanum kinematics
- DC motors
- Encoders
- Odometry
- PID control
- Servomotors
- Raspberry Pi
- ROS2 *(current project)*

</td>
<td width="33%" valign="top">

### 🔬 Electronics & FPGA

- KiCad
- PCB design
- VHDL
- Quartus Prime
- ModelSim
- Cyclone V / DE10-Standard
- SolidWorks
- Hardware prototyping

</td>
</tr>
</table>

---

## Core technologies

<p align="center">
  <img src="https://img.shields.io/badge/C-Embedded%20Development-A8B9CC?style=for-the-badge&logo=c&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-Automation%20%26%20Supervision-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/STM32-Microcontrollers-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white" />
  <img src="https://img.shields.io/badge/Raspberry%20Pi-High--level%20Control-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/VHDL-FPGA-555555?style=for-the-badge" />
  <img src="https://img.shields.io/badge/KiCad-PCB%20Design-314CB0?style=for-the-badge&logo=kicad&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-Development-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ROS2-Robotics-22314E?style=for-the-badge&logo=ros&logoColor=white" />
  <img src="https://img.shields.io/badge/FreeRTOS-Real--Time%20OS-2C9A42?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CAN-Embedded%20Networking-00599C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Quartus%20Prime-FPGA-0071C5?style=for-the-badge&logo=intel&logoColor=white" />
</p>

---

# Selected engineering projects

## 🤖 TopoBot — Autonomous topographic robot

<a href="https://github.com/Mickael235/topobot">
  <img src="https://raw.githubusercontent.com/Mickael235/topobot/main/assets/images/topobot-hero.png"
       alt="TopoBot"
       width="100%">
</a>

**Engineering team project — ENSIM × ESGT**

TopoBot is a holonomic Mecanum robot designed to automate repetitive topographic measurement tasks.

The system combines:

`STM32 F446RE` · `Raspberry Pi` · `C` · `Python` · `Mecanum wheels` · `Encoders` · `Odometry` · `PID` · `AX-12` · `XBee` · `KiCad`

### What the project demonstrates

- distributed embedded architecture between **STM32 and Raspberry Pi**
- real-time robot motion control
- encoder-based odometry
- Mecanum kinematics
- mission waypoint execution
- prism deployment using an AX-12 servomotor
- XBee communication with the total-station workflow
- custom control electronics
- tablet-oriented mission supervision
- system integration and physical testing

### My contribution

My work focused mainly on:

- robot movement development and validation
- trajectory testing
- exploitation of encoder feedback
- motion-error analysis
- contribution to odometry and motion-control integration
- mission-point / trajectory handling
- prototype testing and debugging

[**Explore the TopoBot repository →**](https://github.com/Mickael235/topobot)

---

## ⚡ Distributed STM32 Motor Control

**Personal project in a two-person team — in progress**

A distributed real-time motor-control platform built around STM32.

`STM32` · `C` · `FreeRTOS` · `CAN` · `PID` · `PWM` · `Encoder` · `Python`

The objective is to build an embedded architecture capable of:

- measuring motor speed
- regulating speed using closed-loop control
- exchanging commands and telemetry over CAN
- supervising system state
- detecting communication or hardware faults
- moving the system toward a safe state when required

This project is also an opportunity to work on real-time task organization, CAN message design, diagnostics and fault handling.

[**Explore the project →**](https://github.com/Mickael235/stm32-distributed-motor-control)

---

## 🔬 FPGA / VHDL Digital Systems

Digital-system design and hardware validation on a **Terasic DE10-Standard / Cyclone V FPGA**.

`VHDL` · `Quartus Prime` · `ModelSim` · `Cyclone V` · `DE10-Standard`

Implemented and validated topics include:

- multiplexers
- seven-segment decoding
- binary and BCD arithmetic
- ripple-carry adders
- registers and sequential logic
- hardware counters
- Quartus LPM components
- physical validation using switches, LEDs and seven-segment displays

[**Explore the FPGA/VHDL repository →**](https://github.com/Mickael235/fpga-vhdl-digital-systems)

---

## 📡 Automated Instrumentation Platform

Automated frequency-response measurement platform developed through two successive implementations:

**LabVIEW → LabWindows/CVI / ANSI C**

`LabVIEW` · `LabWindows/CVI` · `C` · `VISA` · `GPIB` · `SCPI` · `TCP/IP`

The platform includes:

- remote function-generator control
- automated multimeter acquisition
- configurable frequency sweeps
- gain computation
- Bode magnitude plotting
- cutoff-frequency estimation
- TCP/IP client-server architecture

This project reflects my interest in **test automation, instrumentation and hardware/software interaction**.

[**Explore the instrumentation repository →**](https://github.com/Mickael235/automated-instrumentation-platform)

---

## 🌡️ PIC16F1719 Temperature Control

Embedded temperature-monitoring and threshold-control system running on a **PIC16F1719 / Explorer 8** platform.

`PIC16F1719` · `Embedded C` · `TMP36` · `ADC` · `LCD` · `PWM` · `PPS`

The system performs:

- temperature acquisition using a TMP36 sensor
- 10-bit ADC conversion
- 8-sample averaging
- user-configurable setpoint acquisition
- LCD feedback
- three-state warning logic
- PWM-based critical-temperature indication

A significant part of the project involved identifying and correcting real hardware acquisition issues.

[**Explore the PIC16F1719 repository →**](https://github.com/Mickael235/pic16f1719-temperature-control)

---

## 💡 STM32 Smart Lighting System

Embedded sensing and actuator-control project based on a **NUCLEO-L496ZG**.

`STM32` · `C` · `GPIO` · `ADC` · `PWM` · `UART` · `PIR` · `LDR`

Three subsystems were validated independently:

- PIR presence detection
- ambient-light acquisition through ADC
- servo control through hardware PWM

The project also documents the integration issues encountered when combining timing-sensitive subsystems and the architectural improvements required for a more robust implementation.

[**Explore the STM32 project →**](https://github.com/Mickael235/stm32-smart-lighting-system)

---

## 🔐 Biometric Access-Control System

**Electronic and mechanical design project**

`PIC16F88` · `SFM3050-TC1` · `MAX232` · `RS232` · `KiCad` · `PCB Design` · `SolidWorks`

The project covers:

- biometric access-control architecture
- PIC16F88-based control design
- RS232 interface design
- relay outputs
- regulated 5 V / 3.3 V power rails
- custom KiCad symbol creation
- PCB placement and routing
- 3D PCB verification
- parametric enclosure design
- electronic / mechanical integration

The PCB and enclosure were completed digitally but were **not physically manufactured**, which is explicitly documented in the repository.

> Repository publication in progress.

---

# What I am working on now

<table>
<tr>
<td width="33%" valign="top">

### ⚙️ Real-time motor control

STM32-based distributed motor-control platform.

Current focus:

- encoder feedback
- PID control
- FreeRTOS architecture
- CAN communication
- diagnostics
- fault handling

</td>
<td width="33%" valign="top">

### 🦾 ROS2 robotic-arm digital twin

Current work around:

- ROS2 Jazzy
- URDF / Xacro
- RViz2
- Gazebo Harmonic
- ros2_control
- MoveIt2

The project is being developed progressively and will be published as the simulation becomes sufficiently complete.

</td>
<td width="33%" valign="top">

### 🔐 TinyML robustness

5th-year research project:

**Evaluation of TinyML robustness through hardware fault injection**

Focus:

- embedded AI
- microcontrollers
- hardware fault injection
- robustness evaluation
- ChipWhisperer-based experimentation

</td>
</tr>
</table>

---

# How I approach engineering

I try to structure projects around a repeatable workflow:

```text
Understand the requirement
        ↓
Define the architecture
        ↓
Implement one subsystem
        ↓
Test it independently
        ↓
Measure / diagnose failures
        ↓
Integrate progressively
        ↓
Document the result
        ↓
Identify limitations and next steps
```

I prefer repositories that show not only the final result, but also:

- the system architecture
- source code
- hardware setup
- testing strategy
- experimental results
- known limitations
- technical documentation

For me, a useful engineering project should make it possible to answer:

> **What was built? How does it work? How was it validated? What failed? What would be improved next?**

---

# What I can discuss in an interview

### Embedded software

- peripheral configuration on STM32 / PIC16
- ADC, PWM, UART and GPIO
- real-time control architecture
- state machines
- FreeRTOS task organization
- CAN communication design

### Robotics

- Mecanum kinematics
- encoder feedback
- odometry
- motor-control loops
- actuator integration
- mission execution

### FPGA

- VHDL design
- combinational / sequential logic
- Quartus synthesis
- ModelSim simulation
- hardware validation on DE10-Standard

### Electronics

- KiCad schematics and PCB layout
- custom symbols / footprints
- power and signal integration
- electronic / mechanical co-design

### Instrumentation

- VISA / GPIB / SCPI
- automated measurements
- frequency sweeps
- Bode response
- TCP/IP client-server supervision

---

# Education

### ENSIM — Le Mans University

**Engineering degree — Embedded and Intelligent Systems**

Current focus:

- embedded systems
- real-time systems
- robotics
- FPGA
- industrial computing
- electronics

---

# Beyond coursework

- 🤖 Member of **ENSIMelec**, ENSIM's robotics team
- 🏆 Participation around the **Coupe de France de Robotique**
- 🧩 Interested in embedded architecture, robotics and system integration
- 📚 I use personal projects to go beyond the academic curriculum and strengthen practical engineering skills

---

# Internship

I am currently looking for a:

### **6-month final-year engineering internship starting in March 2027**

I am particularly interested in roles involving:

- embedded software
- real-time systems
- robotics
- low-level software
- microcontrollers
- FPGA
- control systems
- embedded electronics
- validation / test engineering

Mobility: **France**

---

# Contact

<p align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-essomba--michael-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/essomba-michael-84b12643b/)

[![University Email](https://img.shields.io/badge/University%20Email-Michael.Essomba__Jabe.Etu%40univ--lemans.fr-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Michael.Essomba_Jabe.Etu@univ-lemans.fr)

[![GitHub](https://img.shields.io/badge/GitHub-Mickael235-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mickael235)

</p>

---

<div align="center">

### Thanks for visiting my profile.

**If you are recruiting for embedded systems, robotics or real-time engineering, feel free to explore the projects above and contact me.**

</div>
