# Morse Potential Problem

This repository contains images and explanations related to a physics problem involving the **Morse Potential** function, which approximates the potential energy of two atoms in a molecule.

## 📂 Contents
- **`Screenshot_2025-03-18_9.09.36_PM.png`** – Problem statement.
- **`Screenshot_2025-03-18_9.09.47_PM.png`** – Solution with Taylor expansion and equilibrium separation.

## 📖 Problem Statement
The potential energy of two atoms in a molecule can be approximated by the **Morse Potential**:

\[
U(r) = A \left[ \left(e^{(R-r)/S} - 1 \right)^2 - 1 \right]
\]

where:
- \( r \) is the distance between the two atoms.
- \( A, R, S \) are positive constants with \( S \ll R \).

### 🔹 Tasks
1. **Sketch** \( U(r) \) for \( 0 < r < \infty \).
2. **Find the equilibrium separation** \( r_0 \), where \( U(r) \) is minimized.
3. **For small displacements** \( r = r_0 + x \), show that \( U \) takes the quadratic form:
   \[
   U \approx \text{const} + \frac{1}{2} k x^2
   \]
   confirming Hooke’s Law.
4. **Find the force constant** \( k \).

## 📌 Solution Summary
- The equilibrium separation is found at \( r = R \), meaning \( r_0 = R \).
- Taylor expanding the exponential term in \( U \), the energy function simplifies to a quadratic form, confirming Hooke’s Law.
- The force constant is given by:

  \[
  k = \frac{2A}{S^2}
  \]

This result shows that for small oscillations around equilibrium, the Morse potential behaves like a harmonic oscillator.

## 📜 Usage
This repository is useful for:
- **Physics students** studying molecular bonding and potential energy functions.
- **Quantum mechanics researchers** analyzing vibrational states.
- **Computational physics** applications in molecular simulations.

---

📌 **Contributions & Issues**  
Feel free to contribute by submitting a pull request or opening an issue if you find any errors or have suggestions!

📧 **Contact:** If you have any questions, reach out via GitHub.

---

🚀 **Happy Physics!**
