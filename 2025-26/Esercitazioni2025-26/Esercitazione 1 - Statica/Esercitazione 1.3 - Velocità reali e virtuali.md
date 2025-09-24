
Cognome:

Nome:

## Dichiarazione

Dichiaro che lo svolgimento di questa esercitazione è frutto del mio lavoro.

Data:

Firma:

## Indicazioni
Questa pagina va stampata e le risposte vanno scritte a mano nello spazio a disposizione sotto ogni domanda. Non si può superare lo spazio a disposizione.

## Riferimenti
- Appunti prof. Teresi
- DiBienedetto, Classical Mechanics
- Paroni, Sezione 2.2


## Sistemi di punti materiali vincolati
Il moto di un sistema finito di punti materiali può essere descritto specificando la posizione $P_i$ di ciascuno di essi.

Un vincolo è una restrizione a priori sul moto dei punti materiali. In particolare, un vincolo bilatero può essere scritto come sistema di $j$ equazioni scalari: $$ f_j(P_1,\ldots,P_n,t)=0 \quad (j=1,\ldots,m)
$$In alternativa, la posizione di ciascun punto può essere espressa in funzione di un numero definito di parametri, detti coordinate generalizzate ($q_1, \ldots, q_k$): $$ P_i = P_i(q_1,\ldots, q_k,t) \quad (i=1,\ldots,n) $$ In questo contesto, $q_1, \ldots, q_k$ sono le coordinate generalizzate.

Il numero di equazioni scalari indipendenti imposte dal vincolo prende il nome di "molteplicità del vincolo".

In ogni istante $t$, le condizioni di vincolo precedentemente definite per le posizioni implicano anche restrizioni sulle velocità $\mathbf v(P_k,t)=\frac{d P_k}{d t}$ che i punti possono assumere. Tali restrizioni sulle velocità si ottengono derivando rispetto al tempo le condizioni di vincolo: $$ \sum_{k=1}^n \frac{\partial f_j}{\partial P_k}\cdot\mathbf v(P_k)+\frac{\partial f_j}{\partial t}=0 \quad (j=1,\ldots,m) $$

## Velocità reali di un sistema di punti materiali


In ogni istante $t$, le condizioni di vincolo per le posizioni implicano anche restrizioni sulle velocità $\dot{P}_k(t)=\frac{d P_k}{d t}$ che i punti possono assumere. Tali restrizioni si ottengono derivando rispetto al tempo le condizioni di vincolo: $$ \sum_{k=1}^n \frac{\partial f_j}{\partial P_k}\cdot \dot{P}_k(t)+\frac{\partial f_j}{\partial t}=0 \quad (j=1,\ldots,m) $$ L'insieme delle velocità che soddisfano queste equazioni sono definite come velocità reali compatibili con i vincoli. Esse costituiscono una varietà affine, che può essere rappresentata parametricamente differenziando le equazioni che definiscono le posizioni in termini di coordinate generalizzate: $$ \dot{P}_i(t)=\sum_{l=1}^k \frac{\partial P_i}{\partial q_l}\dot{q}_l(t)+\frac{\partial P_i}{\partial t}. $$
## Velocità virtuali di un sistema di punti materiali

Fissato un istante $t$ e una configurazione $P_1(t), \ldots, P_n(t)$ compatibile con i vincoli, le velocità virtuali sono per definizione tutte e sole le $n$-uple $\mathbf{v}_1, \ldots, \mathbf{v}_n$ che soddisfano il sistema di equazioni: $$ \sum_{k=1}^n \frac{\partial f_j}{\partial P_k} \cdot \mathbf{v}_k=0 \quad(j=1, \ldots, m) $$ Nei testi di meccanica razionale si afferma che le velocità virtuali si ottengono "congelando" i vincoli, ovvero considerando le derivate temporali delle funzioni di vincolo con il tempo mantenuto costante. Mentre le velocità reali formano uno spazio affine (in quanto le equazioni di vincolo sulle velocità possono includere termini non omogenei dipendenti dal tempo), le velocità virtuali costituiscono uno spazio vettoriale. 

Tale spazio ammette la parametrizzazione: $$ \mathbf{v}_i=\sum_{l=1}^k \frac{\partial P_i}{\partial q_l} v_l $$dove le $v_l$ prendono il nome di velocità generalizzate virtuali (o "velocità generalizzate libere"). Si noti che anche la parametrizzazione delle velocita' virtuali si ottiene a partire da quella per le velocità reali, congelando i vincoli, e sostituendo alle derivate temporali $\dot q_l$ delle coordinate libere, le velocità $v_l$ .


## Sistemi continui
I sistemi materiali studiati nella meccanica dei solidi e delle strutture non sono necessariamente discreti, ovvero costituiti da un numero finito di punti. Al contrario, sono solitamente sistemi continui, formati da un insieme di punti materiali che può essere messo in relazione biunivoca con una varietà differenziabile di dimensione 1, 2 o 3.

Per questi corpi, la configurazione è descritta da una deformazione $\mathbf{f}:\Omega\to\mathcal{E}$ che associa a ogni punto $\mathbf{x}$ di una configurazione di riferimento $\Omega$ del corpo la posizione $\mathbf{f}(\mathbf{x})$ di tale punto nello spazio euclideo (si veda il testo di Paroni). In questo contesto, la rappresentazione di una condizione di vincolo può risultare più complessa.

Il più semplice vincolo per un corpo continuo è quello di rigidità, che impone:
$$
|f(\mathbf x)-f(\mathbf y)|=|\mathbf x-\mathbf y|.
$$
## Problema
Dimostrare che se una deformazione è rigida allora ammette la seguente rappresentazione
$$\mathbf{f}(\mathbf{x})=\mathbf{f}\left(\mathbf{x}_0\right)+\mathbf{Q}\left[\mathbf{x}-\mathbf{x}_0\right] \quad \text{ per ogni }\quad \mathbf{x}_0 \in \Omega
$$
dove $\mathbf Q$ è una matrice di rotazione.
### Suggerimento
La dimostrazione si trova in uno dei libri indicati come riferimento.
## Svolgimento

---
---
---
---
---
---
---
---
---
---
---
---
---
---
------
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---

## Coordinate generalizzate per il corpo rigido
Dato che le rotazioni nello spazio sono parametrizzabili con tre coordinate e la posizione del punto $\mathbf{x}_0$ dipende anch'essa da tre parametri, un corpo rigido nello spazio possiede 6 gradi di libertà.

Per ottenere i campi di velocità compatibili con il vincolo di rigidità, si possono seguire due approcci principali:

1. Derivare rispetto al tempo la condizione di vincolo, ottenendo la formula più generale per il campo di velocità. 
2. Derivare rispetto al tempo la parametrizzazione, trattando $\mathbf{f}(\mathbf{x}_0)$ e $\mathbf{Q}$ come coordinate generalizzate.


## Problema

Dimostrare che, se un corpo è rigido, il suo campo di velocità $\mathbf{v}(P)$ ammette la forma:

$$ \mathbf{v}(P)=\mathbf w+\boldsymbol{\omega}\times(P-O)$$
Concludere che $\mathbf w$ e $\boldsymbol\omega$ costituiscono una possibile scelta di velocità generalizzate per il corpo rigido.

### Suggerimento
Adoperando il secondo approccio menzionato, si differenzi rispetto al tempo la formula di rappresentazione della deformazione rigida, ottenendo:
$$ \dot{\mathbf{f}}(\mathbf{x})=\dot{\mathbf{f}}(\mathbf{x}_0)+\dot{\mathbf{Q}}[\mathbf{x}-\mathbf{x}_0] $$
Si indichi con $P=\mathbf{f}(\mathbf{x})$ la posizione occupata dal punto materiale $\mathbf{x}$ nella configurazione attuale. Si indichi inoltre con $O=\mathbf{f}(\mathbf{x}_0)$ la posizione occupata dal punto materiale $\mathbf{x}_0$ nella configurazione attuale.

Si dimostri che, poiché $\mathbf{Q}$ è una matrice ortogonale, vale la relazione:
$$ \mathbf{x}=\mathbf{x}_0+\mathbf{Q}^T(P-O) $$
Si utilizzi il fatto che $\dot{\mathbf{Q}}\mathbf{Q}^T$ è un tensore antisimmetrico e che a questo tensore antisimmetrico si può associare (si vedano le dispense del prof. Teresi) un vettore assiale $\boldsymbol{\omega}$ in modo che:
$$ \dot{\mathbf{Q}}\mathbf{Q}^T(P-O)=\boldsymbol{\omega}\times (P-O). $$
## Svolgimento

---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---


