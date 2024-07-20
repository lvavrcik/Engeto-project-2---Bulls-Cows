# Engeto-project-2---Bulls&Cows
Kód pro 2. Engeto projekt - hra Bulls & Cows

# Bulls & Cows game #
## Popis projektu ##
Cílem tohoto projektu je vytvořit program simulující hru Bulls&Cows. 
Hřáč má za úkol rozluštit tajné čtyřciferné číslo.

**Popis programu**: 
- program pozdraví uživatele a vypíše úvodní text
- program vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
- hráč hádá číslo. Program jej upozorní, pokud:
    - zadá číslo kratší nebo delší než 4 čísla
    - bude číslo obsahovat duplicity
    - bude číslo začínat nulou
    - bude číslo obsahovat nečíselné znaky
    
- program vyhodnotí tip uživatele
- program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows)
- jakmile hráč číslo uhodne, program mu pogratuluje a ukončí se

- program rovněž počítá počet hráčových pokusů + na základě jejich počtu hodnotí jeho hru

**Hodnoty na škále**:
- počet pokusů <= 5 - Wow, amazing
- počet pokusů <= 10 - Very good score
- počet pokusů <= 15 - Not too bad
- počet pokusů <= 20 - Not so good
- počet pokusů > 20 - Time to practice