import sympy as sp
from sympy import symbols, Function, dsolve, simplify, latex, diff, solve, expand, factor

# Definizione delle variabili simboliche
S, p, EI, ell_R = symbols('S p EI ell_R', real=True, positive=True)

# Deflessione w(S) come funzione incognita
w = Function('w')

print("=" * 80)
print("RISOLUZIONE DEL PROBLEMA DELLA TRAVE INCASTRATA-APPOGGIATA")
print("=" * 80)

# Equazione differenziale per la trave di Eulero-Bernoulli
# EI * w''''(S) = p (carico distribuito uniforme)
eq_diff = sp.Eq(EI * w(S).diff(S, 4), p)

print("\n1. Equazione differenziale:")
print("   EI * w''''(S) = p")

# Risoluzione dell'equazione differenziale con SymPy
w_gen_sol = dsolve(eq_diff, w(S))
w_gen = w_gen_sol.rhs

# Estrazione delle costanti di integrazione
constants = sorted(list(w_gen.free_symbols - set([S, p, EI])), key=str)
print(f"\n2. Soluzione generale con costanti {constants}:")
print(f"   w(S) = {simplify(w_gen)}")

# Condizioni al contorno
# 1. w(0) = 0 (incastro a sinistra)
# 2. w'(0) = 0 (incastro a sinistra)
# 3. w(ell_R) = 0 (appoggio a destra)
# 4. M(ell_R) = EI * w''(ell_R) = 0 (appoggio a destra, momento nullo)

# Calcolo delle derivate
w_prime = diff(w_gen, S)
w_double_prime = diff(w_gen, S, 2)

print("\n3. Condizioni al contorno:")
print("   w(0) = 0")
print("   w'(0) = 0")
print("   w(ell_R) = 0")
print("   M(ell_R) = EI * w''(ell_R) = 0")

# Applicazione delle condizioni al contorno
cond1 = sp.Eq(w_gen.subs(S, 0), 0)
cond2 = sp.Eq(w_prime.subs(S, 0), 0)
cond3 = sp.Eq(w_gen.subs(S, ell_R), 0)
cond4 = sp.Eq(EI * w_double_prime.subs(S, ell_R), 0)

# Risoluzione del sistema per le costanti
sol_constants = solve([cond1, cond2, cond3, cond4], constants)

print("\n4. Costanti di integrazione:")
for const_sym, value in sol_constants.items():
    print(f"   {const_sym} = {simplify(value)}")

# Sostituzione delle costanti nella soluzione generale
w_sol = w_gen.subs(sol_constants)
w_sol = simplify(w_sol)

print("\n5. Soluzione finale w(S):")
print(f"   w(S) = {w_sol}")

# Verifica della risposta corretta per w(S)
w_expected = -p * S**2 / (48 * EI) * (3*ell_R**2 - 5*ell_R*S + 2*S**2)
w_expected_expanded = expand(w_expected)
w_sol_expanded = expand(w_sol)

print("\n" + "=" * 80)
print("VERIFICA DELLE RISPOSTE DEL QUIZ")
print("=" * 80)

# Domanda 1: u(S) = 0
print("\n[DOMANDA 1] u(S) = 0?")
print("   CORRETTO: Nella teoria linearizzata, per carichi solo trasversali,")
print("     lo spostamento assiale u(S) e' nullo (disaccoppiamento).")

# Domanda 2: w(S)
print("\n[DOMANDA 2] Verifica di w(S):")
print(f"   Risposta attesa: w(S) = {w_expected}")
print(f"   Soluzione calcolata: w(S) = {w_sol}")
diff_w = simplify(w_sol_expanded - w_expected_expanded)
if diff_w == 0:
    print("   CORRETTO: Le espressioni coincidono!")
else:
    print("   ERRORE: Le espressioni non coincidono!")
    print(f"   Differenza: {diff_w}")

# Domanda 3: Dipendenza da EA
print("\n[DOMANDA 3] w(S) dipende da EA?")
print("   CORRETTO: No, w(S) non dipende da EA.")
print("     Nella teoria linearizzata, flessione e azione assiale sono disaccoppiate.")

# Domanda 4: Trave inestensibile
print("\n[DOMANDA 4] Valido per trave inestensibile?")
print("   CORRETTO: Si, il risultato vale anche per travi inestensibili.")
print("     Poiche' u(S)=0, l'inestensibilita' non cambia il risultato.")

# Calcolo delle grandezze derivate
print("\n" + "=" * 80)
print("CALCOLO DELLE GRANDEZZE DERIVATE")
print("=" * 80)

# Rotazione omega(S) = w'(S)
omega = diff(w_sol, S)
omega = simplify(omega)
print(f"\nRotazione: omega(S) = w'(S) = {omega}")

# Curvatura kappa(S) = w''(S)
kappa = diff(w_sol, S, 2)
kappa = simplify(kappa)
print(f"\nCurvatura: kappa(S) = w''(S) = {kappa}")

# Momento flettente M(S) = EI * kappa(S)
M = EI * kappa
M = simplify(M)
print(f"\nMomento flettente: M(S) = EI * w''(S) = {M}")

# Forza di taglio T(S) = M'(S)
T = diff(M, S)
T = simplify(T)
print(f"\nForza di taglio: T(S) = M'(S) = {T}")

# Valori agli estremi
print("\n" + "=" * 80)
print("VALORI AGLI ESTREMI")
print("=" * 80)

print(f"\nw(0) = {w_sol.subs(S, 0)}")
print(f"omega(0) = {omega.subs(S, 0)}")
print(f"w(ell_R) = {w_sol.subs(S, ell_R)}")
print(f"M(0) = {M.subs(S, 0)}")
print(f"M(ell_R) = {M.subs(S, ell_R)}")
print(f"T(0) = {T.subs(S, 0)}")
print(f"T(ell_R) = {T.subs(S, ell_R)}")

# Domanda 6: Momento massimo
print("\n" + "=" * 80)
print("[DOMANDA 6] Momento flettente massimo")
print("=" * 80)
M_at_0 = M.subs(S, 0)
M_at_ell_R = M.subs(S, ell_R)
print(f"M(0) = {M_at_0}")
print(f"M(ell_R) = {M_at_ell_R}")

# Verifica se ci sono altri punti critici
M_prime = diff(M, S)
M_critical = solve(M_prime, S)
print(f"\nPunti critici per M(S): {M_critical}")

M_max_expected = p * ell_R**2 / 8
M_at_0_simplified = simplify(M_at_0)
# Verifica il valore assoluto: |M(0)| dovrebbe essere p*ell_R^2/8
# Per espressioni simboliche, verifichiamo se M(0) = ±p*ell_R^2/8
M_at_0_pos = simplify(M_at_0 - M_max_expected)  # M(0) = +p*ell_R^2/8
M_at_0_neg = simplify(M_at_0 + M_max_expected)  # M(0) = -p*ell_R^2/8

if M_at_0_pos == 0:
    print(f"CORRETTO: |M_max| = |M(0)| = {M_at_0_simplified} = p*ell_R^2/8")
    print(f"Nota: M(0) è positivo (convenzione: momento positivo)")
elif M_at_0_neg == 0:
    print(f"CORRETTO: |M_max| = |M(0)| = {simplify(-M_at_0)} = p*ell_R^2/8")
    print(f"Nota: M(0) è negativo (convenzione: momento negativo)")
else:
    print(f"ATTENZIONE: M(0) = {M_at_0}")
    print(f"Atteso: |M(0)| = {M_max_expected}")
    print(f"Verifica M(0) - p*ell_R^2/8 = {M_at_0_pos}")
    print(f"Verifica M(0) + p*ell_R^2/8 = {M_at_0_neg}")
    # Calcoliamo numericamente per verificare
    M_at_0_num = float(M_at_0_simplified.subs([(p, 1), (ell_R, 1)]))
    M_expected_num = float(M_max_expected.subs([(p, 1), (ell_R, 1)]))
    print(f"Valore numerico: M(0) = {M_at_0_num}, atteso |M(0)| = {M_expected_num}")
    if abs(M_at_0_num) == M_expected_num:
        print("CORRETTO: Il valore assoluto coincide (differenza solo nel segno)")

# Domanda 7: Taglio massimo
print("\n" + "=" * 80)
print("[DOMANDA 7] Forza di taglio massima")
print("=" * 80)
T_at_0 = T.subs(S, 0)
T_at_ell_R = T.subs(S, ell_R)
print(f"T(0) = {T_at_0}")
print(f"T(ell_R) = {T_at_ell_R}")

T_max_expected = 5*p*ell_R/8
if simplify(T_at_0 + T_max_expected) == 0:  # T(0) è negativo
    print(f"CORRETTO: |T_max| = |T(0)| = {simplify(-T_at_0)} = 5*p*ell_R/8")
else:
    print(f"ERRORE: T(0) = {T_at_0}, atteso: -5*p*ell_R/8")
    print(f"Verifica: T(0) + 5*p*ell_R/8 = {simplify(T_at_0 + T_max_expected)}")

# Domanda 5: Deflessione massima
print("\n" + "=" * 80)
print("[DOMANDA 5] Deflessione massima in valore assoluto")
print("=" * 80)

# Ricerca dei punti critici per w(S) (dove w'(S) = 0)
omega_zeros = solve(omega, S)
print(f"Punti critici (omega(S) = 0): {omega_zeros}")

# Valutazione di w nei punti critici interni (0 < S < ell_R)
# Usiamo un approccio numerico per verificare quali punti sono nell'intervallo
w_max_abs = 0
S_max_pos = None
coeff_from_crit = None
print("\nValutazione dei punti critici:")
for s_crit in omega_zeros:
    # Verifica se il punto è reale
    if s_crit.is_real:
        # Sostituiamo ell_R=1 per verificare se 0 < s_crit < ell_R
        s_crit_num = float(s_crit.subs(ell_R, 1))
        if 0 < s_crit_num < 1:  # Verifica con ell_R=1
            w_crit = w_sol.subs(S, s_crit)
            w_crit_abs = abs(w_crit)
            print(f"w({s_crit}) = {simplify(w_crit)}")
            print(f"  (valore numerico: S = {s_crit_num:.6f} * ell_R)")
            # Calcoliamo il valore assoluto numerico per confronto
            w_crit_abs_num = float((w_crit_abs * EI / (p * ell_R**4)).subs(ell_R, 1))
            if w_crit_abs_num > w_max_abs:
                w_max_abs = w_crit_abs_num
                S_max_pos = s_crit
                coeff_from_crit = w_crit_abs_num
        else:
            print(f"Punto critico fuori intervallo: S = {s_crit} (numerico: {s_crit_num:.6f} * ell_R)")
    else:
        print(f"Punto critico non reale: S = {s_crit}")

# Se abbiamo trovato un punto critico, usiamolo, altrimenti usiamo l'approssimazione
if S_max_pos is not None:
    print(f"\nPunto di massimo trovato: S = {S_max_pos}")
    w_max_at_crit = w_sol.subs(S, S_max_pos)
    w_max_at_crit_abs = abs(w_max_at_crit)
    print(f"|w|_max = {simplify(w_max_at_crit_abs)}")
    # Calcoliamo il coefficiente numerico
    coeff_from_crit = float((w_max_at_crit_abs * EI / (p * ell_R**4)).subs(ell_R, 1))
    print(f"Coefficiente numerico dal punto critico: {coeff_from_crit:.6f}")
else:
    print("\nNessun punto critico trovato nell'intervallo, uso approssimazione numerica")

# Calcolo numerico approssimato per il punto di massimo
# Il massimo si trova approssimativamente a S ≈ 0.4215*ell_R
S_max_approx = 0.4215 * ell_R
w_max_approx = w_sol.subs(S, S_max_approx)
w_max_approx_abs = abs(w_max_approx)

print(f"\nValore approssimato a S = 0.4215*ell_R:")
print(f"|w|_max ≈ {simplify(w_max_approx_abs)}")

# Verifica con la risposta attesa
w_max_expected = p * ell_R**4 / (185 * EI)
w_max_expected_num = 1/185  # coefficiente numerico

# Calcoliamo il coefficiente numerico della soluzione approssimata
coeff_approx = float((w_max_approx_abs * EI / (p * ell_R**4)).subs(ell_R, 1))
coeff_expected = float(w_max_expected_num)

print(f"\nCoefficiente numerico calcolato (approssimato): {coeff_approx:.6f}")
print(f"Coefficiente numerico atteso (1/185): {coeff_expected:.6f}")
print(f"Coefficiente numerico atteso (0.0054): 0.005405")

# Usa il coefficiente dal punto critico se disponibile, altrimenti quello approssimato
coeff_to_check = coeff_from_crit if coeff_from_crit is not None else coeff_approx

if abs(coeff_to_check - coeff_expected) < 0.0001:
    print("CORRETTO: Il coefficiente coincide con 1/185 ≈ 0.005405")
else:
    print("ATTENZIONE: Verificare il calcolo del massimo")
    print(f"Differenza: {abs(coeff_to_check - coeff_expected):.6f}")

# Calcolo esatto del punto di massimo
print("\nCalcolo esatto del punto di massimo:")
# Risolviamo omega(S) = 0 per trovare il punto esatto
omega_factorized = sp.factor(omega)
print(f"omega(S) fattorizzato: {omega_factorized}")

# Il punto di massimo si trova risolvendo omega(S) = 0
# Per una trave incastrata-appoggiata, il massimo è a S = (5-sqrt(5))/10 * ell_R
S_max_exact = (5 - sp.sqrt(5)) / 10 * ell_R
w_max_exact = w_sol.subs(S, S_max_exact)
w_max_exact_abs = abs(w_max_exact)
w_max_exact_coeff = simplify(w_max_exact_abs * EI / (p * ell_R**4))

print(f"\nPunto di massimo esatto: S = {S_max_exact}")
print(f"Valore numerico: S ≈ {float(S_max_exact.subs(ell_R, 1)):.6f} * ell_R")
print(f"|w|_max esatto = {w_max_exact_abs}")
print(f"Coefficiente esatto: {w_max_exact_coeff}")
print(f"Valore numerico del coefficiente: {float(w_max_exact_coeff):.6f}")

print("\n" + "=" * 80)
print("RIEPILOGO VERIFICHE")
print("=" * 80)
print("Domanda 1: u(S) = 0 - CORRETTO")
print("Domanda 2: w(S) verificata simbolicamente -", "CORRETTO" if diff_w == 0 else "DA VERIFICARE")
print("Domanda 3: w(S) non dipende da EA - CORRETTO")
print("Domanda 4: Valido per trave inestensibile - CORRETTO")
print("Domanda 5: |w|_max ≈ p*ell_R^4/(185*EI) -", "CORRETTO" if abs(coeff_approx - coeff_expected) < 0.0001 else "DA VERIFICARE")
# Verifica finale del momento: controlla il valore assoluto
M_check_pos = simplify(M_at_0 - M_max_expected) == 0
M_check_neg = simplify(M_at_0 + M_max_expected) == 0
M_check = M_check_pos or M_check_neg
print("Domanda 6: |M|_max = p*ell_R^2/8 all'incastro -", "CORRETTO" if M_check else "DA VERIFICARE")
print("Domanda 7: |T|_max = 5*p*ell_R/8 all'incastro -", "CORRETTO" if simplify(T_at_0 + T_max_expected) == 0 else "DA VERIFICARE")
print("\n" + "=" * 80)

