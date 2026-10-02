---
id: HW-01
proof_id: P-1.1
assigned_week: W1
due_week: W3
status: assigned
---

# HW-01 / HW-P-1.1 — Ricostruzione di una curva piana

## Problema

Sia $I$ un intervallo connesso e siano
$\mathbf{x},\widehat{\mathbf{x}}\in C^2(I;\mathbb{R}^2)$ due parametrizzazioni
regolari, definite sullo stesso intervallo e con lo stesso verso di
percorrenza. Supponiamo che abbiano la stessa ascissa curvilinea
$s(\zeta)$ e la stessa curvatura algebrica $\mathrm{C}(\zeta)$:

$$
s'(\zeta)=\|\mathbf{x}'(\zeta)\|
          =\|\widehat{\mathbf{x}}'(\zeta)\|>0,
\qquad
\mathrm{C}(\zeta)=\frac{\alpha'(\zeta)}{s'(\zeta)}
                  =\frac{\widehat{\alpha}'(\zeta)}{s'(\zeta)}.
$$

Dimostrare che esistono un angolo $\theta\in\mathbb{R}$ e un vettore
costante $\boldsymbol{s}\in\mathbb{R}^2$ tali che

$$
\boxed{\mathbf{x}(\zeta)=\boldsymbol{s}+R(\theta)\widehat{\mathbf{x}}(\zeta)},
$$

dove $R(\theta)$ è il tensore di rotazione definito mediante il prodotto
diadico $\otimes$:

$$
R(\theta)=
\cos\theta\,\bigl(\mathbf{e}_1\otimes\mathbf{e}_1
                     +\mathbf{e}_2\otimes\mathbf{e}_2\bigr)
+\sin\theta\,\bigl(\mathbf{e}_2\otimes\mathbf{e}_1
                     -\mathbf{e}_1\otimes\mathbf{e}_2\bigr),
\qquad
(\mathbf a\otimes\mathbf b)\mathbf v
=\mathbf a(\mathbf b\cdot\mathbf v).
$$

## Consegna

Scrivere una dimostrazione completa, esplicitando:

1. l’integrazione di $\alpha'=s'\mathrm{C}$ e
   $\widehat{\alpha}'=s'\mathrm{C}$;
2. la costanza di $\theta=\alpha-\widehat{\alpha}$ su $I$;
3. la relazione tra i versori tangenti e il tensore di rotazione $R(\theta)$, espresso mediante prodotti diadici;
4. la seconda integrazione e la definizione
   $\boldsymbol{s}=\mathbf{x}(\zeta_*)-R(\theta)\widehat{\mathbf{x}}(\zeta_*)$.

Precisare che $\theta$ è definito modulo $2\pi$, che una riflessione non è una
rotazione diretta e che la prova non implica la chiusura globale di una curva.

## Materiale di riferimento

- [M02 — curva piana parametrizzata](../Slides/Marigo/M02.html)
- [Marigo italiano — §1.2, configurazioni di un mezzo continuo curvilineo](https://giuseppetomassetti.github.io/Teaching/marigo-italiano/capitolo-1/1-2-configurazioni-di-un-mezzo-continuo-curvilineo.html)
- [Indice dei risultati di Marigo](https://giuseppetomassetti.github.io/Teaching/marigo-italiano/indice-dei-risultati.html)

Assegnazione: dopo M02. Discussione: due settimane dopo l’assegnazione.
