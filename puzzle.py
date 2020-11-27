from logic import *


AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnave, BKnave),
    Not(And(AKnave, AKnight)),
    Implication(And(AKnave,AKnight), AKnight),
    Implication(Not(And(AKnave,AKnight)), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),

    Implication(And(AKnave,BKnave), AKnight),
    Implication(Not(And(AKnave,BKnave)), AKnave),
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),

    Implication(Or(And(BKnight, AKnight), And(BKnave, AKnave)), AKnight),
    Implication(Not(Or(And(BKnight, AKnight), And(BKnave, AKnave))), AKnave),

    Implication(AKnight, BKnight),
    Biconditional(AKnave, BKnight),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),
    Or(CKnave, CKnight),
    Not(And(CKnight, CKnave)),
    
    # A said I'm a knight
   Or(And(Implication(AKnight, AKnight),Implication(Not(AKnight), AKnave)),
   And(Implication(AKnave, And(AKnave, AKnight)),Implication(Not(AKnave), And(AKnave, Not(AKnave))))
   ),

    Implication(CKnave, BKnight),
    Implication(Not(CKnave), BKnave),


    Implication(Or(Implication(AKnight, AKnight), Implication(Not(AKnight), AKnave)), CKnight),
    Implication(Not(Or(Implication(AKnight, AKnight), Implication(Not(AKnight), AKnave))), CKnave),

    Implication(AKnight, CKnight),
    Implication(Not(AKnight), CKnave)

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
