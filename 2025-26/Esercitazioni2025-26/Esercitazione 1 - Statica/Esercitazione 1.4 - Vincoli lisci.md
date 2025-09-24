
## Dichiarazione

Cognome:

Nome:

Dichiaro che lo svolgimento di questa esercitazione è frutto del mio lavoro.

Data:

Firma:

## Indicazioni
Questa pagina va stampata e le risposte vanno scritte a mano nello spazio a disposizione sotto ogni domanda. Non si può superare lo spazio a disposizione.

## Riferimenti

- Appunti prof. Teresi
- DiBienedetto, Classical Mechanics




## Spostamenti virtuali

In molti testi di meccanica razionale la velocità virtuale è sostituita dallo spostamento virtuale. Le due grandezze descrivono lo stesso oggetto geometrico: un vettore tangente alla varietà dei vincoli nell’istante considerato; differiscono solo per scala/unità. Per definizione, lo spostamento virtuale è uno spostamento infinitesimo $\delta\mathbf f$ compatibile con il vincolo nell’istante dato. Nella Scienza delle Costruzioni si preferisce parlare di spostamento virtuale; tuttavia, è didatticamente più efficace introdurre il concetto tramite le velocità virtuali perché la nozione di vettore tangente emerge più naturalmente dalla derivazione temporale delle equazioni di vincolo.

Nella letteratura della meccanica, la notazione più comune per gli spostamenti virtuali è:

- $\mathbf{\delta r}$: Questa è la notazione più diffusa per indicare uno spostamento virtuale generico di un punto o di una particella. Ad esempio, nel contesto di corpi rigidi, si trova scritto $\mathbf{\delta r}(P)$ per lo spostamento virtuale del punto materiale che occupa la posizione $P$.
- $\mathbf{\delta P}$: Similmente, $\mathbf{\delta P}$ può essere usato per rappresentare lo spostamento virtuale di un punto $P$, in particolare quando si discute di un sistema di punti.
- $\mathbf{\delta q_i}$: Quando si utilizzano coordinate generalizzate $q_i$, lo spostamento virtuale corrispondente viene indicato con $\mathbf{\delta q_i}$.
- $\mathbf{\delta \boldsymbol{\theta}}$: Per le rotazioni virtuali, specialmente nel caso di corpi rigidi, si usa il vettore di rotazione virtuale infinitesima $\mathbf{\delta \boldsymbol{\theta}}$. Nel caso bidimensionale, questo può essere semplicemente $\mathbf{\delta \theta}$.

Queste notazioni indicano spostamenti infinitesmi, immaginari, compatibili con i vincoli del sistema e compiuti istantaneamente (senza variazione di tempo, $\delta t=0$).

Occorre fare attenzione se $P(t)=\mathbf f(\mathbf x,t)$ la legge oraria del punto materiale $\mathbf x$, la velocità è $$ \dot P(t)=\dot{\mathbf f}(\mathbf x,t). $$ Questa funzione descrive, al tempo $t$, il campo di velocità nella configurazione di riferimento. Nella meccanica del corpo rigido, tuttavia, è di interesse la velocità di un punto materiale in funzione della posizione corrente $P(t)$ occupata dal punto. Fissato un posto $P$ la velocità del punto materiale che al tempo occupa il posto $P$ è $\mathbf v(P,t)=\dot{\mathbf f}(\mathbf f^{-1}(P),t)$. Il corrispondente spostamento virtuale è dunque $\delta \mathbf r(P)=\delta{\mathbf f}(\mathbf f^{-1}(P))$

Osserviamo che la variazione $\delta\mathbf f$ è definita sul dominio materiale $\Omega$: per $\mathbf x$ fissato, $\delta\mathbf f(\mathbf x)$ rappresenta lo spostamento (virtuale) del medesimo punto materiale $\mathbf x$. Al contrario, lo spostamento virtuale spaziale $\delta\mathbf r$ è definito sul luogo corrente $\mathbf f(\Omega,t)$: per fissato, $\delta\mathbf r(P)$ è la variazione del posto fisico $P$ (cioè di qualunque particella occupi $P$ in quell’istante). Sono dunque due funzioni diverse perché hanno domini diversi e rispondono a due descrizioni differenti, lagrangiana la prima, euleriana la seconda.

Dal punto di vista operativo, nella meccanica del corpo rigido e nel principio dei lavori virtuali conviene lavorare con $\delta \mathbf{r}(P)$, poiché le forze e i momenti sono applicati in spazio corrente: per esempio $\delta W=\mathbf{R} \cdot \delta \mathbf{r}\left(P_0\right)+\mathbf{M}_{P_0} \cdot \delta \boldsymbol{\theta}$. Al tempo stesso, in formulazioni materiali o quando si impongono vincoli in riferimento, è più naturale usare $\delta \mathbf{f}(\mathbf{x})$. Per evitare ambiguità - e per ricordare a colpo d'occhio quale sia il punto tenuto fisso nella variazione (la particella $\mathbf{x}$ oppure il posto $P$ ) - è buona pratica mantenere notazioni diverse per $\delta \mathbf{f}$ e $\delta \mathbf{r}$.

## Caratterizzazione delle reazioni di un vincolo liscio bilatero

Seguiamo la caratterizzazione data nel testo di DiBenedetto, Cap.5, Sez. 5.

- Le reazioni vincolari erogate da un vincolo liscio bilatero sono tutti e soli i sistemi di forze che compiono lavoro virtuale nullo per ogni atto di moto compatibile con il vincolo.

## Punto materiale vincolato

Nel caso di un punto materiale vincolato, il vincolo liscio è tale che il prodotto scalare tra la forza di reazione vincolare $\mathbf R$ e qualsiasi spostamento virtuale compatibile ( $\delta \mathbf{r}$ ) è sempre zero: $\mathbf{R} \cdot \delta \mathbf{r}=0$.

## Spostamenti Virtuali per un Corpo Rigido Incernierato

Quando un corpo rigido è incernierato in un punto materiale $P$ (che chiameremo $C$ per cerniera), questo vincolo impone che il punto $C$ occupi sempre la medesima posizione. Matematicamente, questo significa che lo spostamento di $C$ è nullo, ovvero $\mathbf{r}_{C}=$ costante. Per uno spostamento virtuale, la condizione imposta dal vincolo di cerniera sul punto $C$ è che il suo spostamento virtuale sia nullo: $$ \delta \mathbf{r}(C)=\mathbf{0} $$ Se scegliamo il punto di cerniera $C$ come polo del nostro riferimento per descrivere gli spostamenti virtuali ( $\mathbf{r}_{P_0}=\mathbf{r}_{C}$ ), allora l'equazione generale degli spostamenti virtuali si semplifica notevolmente. Poiché $\delta \mathbf{r}(C)=\mathbf{0}$, l'espressione diventa: $$ \delta \mathbf{r}(P) = \delta \boldsymbol{\theta} \times\left(\mathbf{r}(P)-\mathbf{r}(C)\right) $$ Questo significa che per un corpo rigido incernierato, gli spostamenti virtuali di qualsiasi altro punto $P$ del corpo sono puramente rotazionali attorno al punto di cerniera $C$. La traslazione virtuale del polo è annullata dalla condizione del vincolo.

## Lavoro meccanico

Ora, dato un sistema di forze $\mathcal F$ applicato a un corpo rigido, e un campo di spostamento virtuale, il lavoro meccanico elementare di tale sistema per lo spostamento virtuale si scrive come: $$ \delta W=\mathbf{R}(\mathcal F) \cdot \delta \mathbf{r}(P_0)+\mathbf{M}_{P_0}(\mathcal F) \cdot \delta \boldsymbol{\theta} $$ dove:

- $\mathbf{R}(\mathcal F)$ è la risultante di tutte le forze esterne applicate al corpo rigido.
- $\delta \mathbf{r}(P_0)$ è lo spostamento virtuale del punto $P_0$ (polo) scelto come riferimento sul corpo rigido; rappresenta la componente traslazionale dello spostamento virtuale
- $\mathbf{M}_{P_0}(\mathcal F)$ è il momento risultante di tutte le forze esterne rispetto al polo $P_0$.
- $\delta \boldsymbol{\theta}$ è il vettore di rotazione virtuale infinitesima del corpo rigido; rappresenta la componente rotazionale dello spostamento virtuale.

Questa formula esprime il fatto che il lavoro virtuale totale compiuto da un sistema di forze su un corpo rigido è dato dalla somma del lavoro virtuale della risultante delle forze per lo spostamento virtuale del polo e del lavoro virtuale del momento risultante per la rotazione virtuale del corpo.

## Reazioni vincolari di un vincolo di tipo "cerniera" applicato a un corpo rigido

Sostituendo la condizione di vincolo $$\delta \mathbf{r}(C)=\mathbf{0}$$nella condizione $$\delta W=0,$$ otteniamo: $$0=\mathbf{R}_{\mathcal{F}} \cdot \mathbf{0}+\mathbf{M}_{C, \mathcal{F}} \cdot \delta \boldsymbol{\theta} \Longrightarrow 0=\mathbf{M}_{C, \mathcal{F}} \cdot \delta \boldsymbol{\theta}.$$Poiché, il vincolo di tipo cerniera permette una rotazione virtuale $\delta \boldsymbol{\theta}$ arbitraria (un corpo incernierato può ruotare liberamente attorno al punto della cerniera), l'unica possibilità per cui il prodotto scalare $\mathbf{M}_{C, \mathcal{F}} \cdot \delta \boldsymbol{\theta}$ sia sempre nullo è che il momento risultante delle reazioni rispetto al punto della cerniera sia nullo: $\mathbf{M}_{C, \mathcal{F}}=\mathbf{0}$

Il risultato $\mathbf{M}_{C, \mathcal{F}}=\mathbf{0}$ è fondamentale. Per i teoremi di riduzione dei sistemi di forze agenti su corpi rigidi, se il momento risultante di un sistema di forze rispetto a un punto è nullo, allora il sistema di forze può essere ridotto a una singola forza risultante applicata in quel punto. Quindi, in una cerniera ideale, il sistema delle reazioni vincolari si riduce a una sola forza $\mathbf{R}_{\mathcal{F}}$ applicata nel punto $C$ della cerniera.

È importante notare che l'applicazione del criterio di vincolo liscio non dice nulla sull'intensità o sulla direzione della risultante $\mathbf{R}_{\mathcal{F}}$. La forza risultante delle reazioni vincolari $\mathbf{R}_{\mathcal{F}}$ può avere qualsiasi componente (su tutti e tre gli assi se la cerniera è libera di ruotare in tutte le direzioni, o meno se ci sono ulteriori vincoli al moto rotatorio), ed è questa forza che bilancerà le forze esterne affinché il punto $C$ rimanga fisso.

## Spostamenti Virtuali di un Corpo Rigido Piano

Un **corpo rigido piano** è un corpo il cui moto è confinato a un piano (ad esempio il piano $xy$). In questo caso, il corpo ha **3 gradi di libertà**:

- 2 traslazioni (lungo $x$ e $y$),
- 1 rotazione attorno a un asse ortogonale al piano (asse $z$).

### Espressione degli spostamenti virtuali

Sia $P$ un punto generico del corpo rigido e $P_0$ un punto di riferimento scelto sul corpo (ad esempio il baricentro). Lo spostamento virtuale di $P$ si scrive come: $$ \delta \mathbf{r}(P) = \delta \mathbf{r}(P_0) + \delta \theta \, \hat{\mathbf{z}} \times \left( \mathbf{r}(P) - \mathbf{r}(P_0) \right), $$ dove:

- $\delta \mathbf{r}(P_0) = (\delta x, \delta y)$ è lo spostamento virtuale di traslazione del punto di riferimento,
- $\delta \theta$ è la rotazione virtuale infinitesima attorno all’asse $z$,
- $\mathbf{r}(P) - \mathbf{r}(P_0)$ è il vettore posizione di $P$ rispetto a $P_0$,
- $\hat{\mathbf{z}}$ è il versore uscente dal piano.

### Interpretazione geometrica

- Tutti i punti del corpo condividono lo stesso spostamento di traslazione $\delta \mathbf{r}(P_0)$.
- In aggiunta, ogni punto descrive uno spostamento virtuale rotazionale proporzionale alla sua distanza da $P_0$, ortogonale al vettore $\mathbf{r}(P) - \mathbf{r}(P_0)$ e al versore $\hat{\mathbf{z}}$.

In altre parole, lo **spostamento virtuale** di un corpo rigido piano è sempre la combinazione di una **traslazione** comune e di una **rotazione infinitesima** attorno a un punto arbitrario del corpo.

## Reazioni vincolari di una Cerniera su un Corpo Rigido Piano

Una **cerniera piana** vincola un corpo rigido a un punto $C$ del piano, impedendo qualsiasi spostamento traslazionale del punto stesso, ma lasciando libera la rotazione del corpo attorno ad esso. Poiché il punto $C$ è fisso: $$ \delta \mathbf{r}(C) = \mathbf{0}, $$ dalla caratterizzazione delle reazioni vincolari $\mathcal{F}$ si ottiene: $$ \delta W = \mathbf{R}(\mathcal{F}) \cdot \delta \mathbf{r}(C) + {M}_{C}(\mathcal{F}) \cdot \delta \theta. $$

Essendo $\delta \mathbf{r}(C) = \mathbf{0}$, risulta: $$ \delta W = {M}_{C}(\mathcal{F}) \cdot \delta \theta. $$

Affinché $\delta W = 0$ per ogni $\delta \theta$, si deve avere: $$ {M}_{C}(\mathcal{F}) = 0. $$ Riassumendo, nel caso di una cerniera piana:

- Il momento della cerniera è nullo.
- La reazione vincolare è costituita **solo da una forza** $\mathbf{R}$, applicata al punto $C$.
- Questa forza $\mathbf{R}$ può avere **due componenti indipendenti** lungo gli assi cartesiani $(R_x, R_y)$.

## Cerniera interna

Una cerniera interna collega due corpi rigidi nello stesso punto $P$. Indichiamo con $\delta \mathbf{r}^{(1)}(P)$ e $\delta \mathbf{r}^{(2)}(P)$ rispettivamente lo spostamento virtuale del punto $P$ del corpo 1 e del corpo 2 . La condizione di vincolo è che i due punti materiali coincidenti restino uniti: $$ \delta \mathbf{r}^{(1)}(P)=\delta \mathbf{r}^{(2)}(P) . $$ Le rotazioni virtuali dei due corpi, invece, sono indipendenti: $\delta \boldsymbol{\theta}^{(1)}, \delta \boldsymbol{\theta}^{(2)}$ arbitrarie.

Dal postulato delle reazioni vincolari, segue che un vincolo che agisce sui due corpi esercita due sistemi di forze: $\mathcal{F}^{(1)}$ e $\mathcal{F}^{(2)}$, rispettivamente sul corpo 1 e sul corpo 2. Sia $\mathbf{R}^{(1)}$ la risultante del sistema di forze $\mathcal{F}^{(1)}$ e $\mathbf{M}_P^{(1)}$ il momento risultante di $\mathcal{F}^{(1)}$ rispetto al punto $P$. Analogamente, sia $\mathbf{R}^{(2)}$ la risultante del sistema di forze $\mathcal{F}^{(2)}$ e $\mathbf{M}_P^{(2)}$ il momento risultante di $\mathcal{F}^{(2)}$ rispetto al punto $P$.

Il lavoro virtuale totale compiuto dalle reazioni è la somma dei lavori virtuali delle reazioni agenti su ciascun corpo. Utilizzando la notazione comune per il lavoro virtuale di un sistema di forze su un corpo rigido (risultante per spostamento virtuale del polo più momento risultante per rotazione virtuale), si ha: $$ \delta W=\left(\mathbf{R}^{(1)} \cdot \delta \mathbf{r}^{(1)}(P)+\mathbf{M}_P^{(1)} \cdot \delta \boldsymbol{\theta}^{(1)}\right)+\left(\mathbf{R}^{(2)} \cdot \delta \mathbf{r}^{(2)}(P)+\mathbf{M}_P^{(2)} \cdot \delta \boldsymbol{\theta}^{(2)}\right) . $$ Poiché la condizione di vincolo impone che $\delta \mathbf{r}^{(1)}(P)=\delta \mathbf{r}^{(2)}(P)=\delta \mathbf{r}(P)$ (dove $\delta \mathbf{r}(P)$ è lo spostamento virtuale comune del punto di cerniera), l'espressione del lavoro virtuale può essere riscritta come:

$$ \delta W=\left(\mathbf{R}^{(1)}+\mathbf{R}^{(2)}\right) \cdot \delta \mathbf{r}(P)+\mathbf{M}_P^{(1)} \cdot \delta \boldsymbol{\theta}^{(1)}+\mathbf{M}_P^{(2)} \cdot \delta \boldsymbol{\theta}^{(2)} . $$ Per una cerniera interna ideale, il lavoro virtuale delle reazioni deve essere nullo ( $\delta W=0$ ) per ogni spostamento virtuale compatibile. Dato che $\delta \mathbf{r}(P), \delta \boldsymbol{\theta}^{(1)}$ e $\delta \boldsymbol{\theta}^{(2)}$ sono indipendenti, ciò implica che i coefficienti di ciascun termine devono essere nulli:

1. $\mathbf{R}^{(1)}+\mathbf{R}^{(2)}=\mathbf{0} \Longrightarrow \mathbf{R}^{(2)}=-\mathbf{R}^{(1)}$ : Questo indica che le forze di reazione che i due corpi si scambiano attraverso la cerniera sono uguali e opposte (principio di azione e reazione), ma la cerniera trasmette forza.
2. $\mathbf{M}_P^{(1)}=\mathbf{0}$
3. $\mathbf{M}_P^{(2)}=\mathbf{0}$ Queste due ultime condizioni stabiliscono che una cerniera interna ideale non trasmette momenti (flettenti o torcenti) tra i corpi rispetto al punto $P$, consentendo una rotazione relativa libera .

## Domanda

Comando Carrello (appoggio semplice) in un sistema di corpi piano

![[../../Excalidraw/Drawing 2025-09-17 21.28.56.excalidraw]]

La figura mostra un corpo rigido piano vincolato a un **carrello** posto nel punto $P$, appoggiato su un piano liscio con **versore normale** $\hat{\mathbf n}$ e **versore tangenziale** $\hat{\mathbf t}$.

Le condizioni cinematiche compatibili sono: $$ \delta \mathbf r(P)\cdot \hat{\mathbf n}=0 \quad\text{(niente spostamento normale)},\qquad \delta \mathbf r(P)\cdot \hat{\mathbf t}\ \text{arbitrario},\qquad \delta \theta\ \text{arbitrario}. $$ Usando la caratterizzazione delle reazioni di un vincolo **ideale** e scrivendo il lavoro virtuale come $$ \delta W \;=\; \mathbf R\cdot \delta \mathbf r(P)\;+\; M_P\,\delta \theta, $$**dedurre** a partire dalla caratterizzazione dei vincoli ideali le restrizioni che devono soddisfare la **risultante** $\mathbf R$ e il **momento risultante** $M_P$ del vincolo di carrello. Carrello (appoggio semplice) in un sistema di corpi piano

### Risposta:

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

## Problema 
Si consideri una cerniera a terra nella quale convergono due aste. 




## Consegna

Per tutti i vincoli interni elencati nel capitolo 3 di Casini e Vasta in figura 3.9 e 3.10, caratterizzare le possibili reazioni vincolari che il vincolo può esercitare usando la caratterizzazione di vincolo liscio.

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
---
---
---
---
---
---

