def get_elo_band(avg_elo):
    if avg_elo <= 900: return "501–900"
    elif avg_elo <= 1300: return "901–1300"
    elif avg_elo <= 1700: return "1301–1700"
    elif avg_elo <= 2100: return "1701–2100"
    elif avg_elo <= 2500: return "2101–2500"
    else: return "2500+"

def get_outcome(result):
    if result == '1-0':
        return 'WhiteWin'
    elif result == '0-1':
        return 'BlackWin'
    else:
        return 'Draw'
        
def describe_opening(eco_code):
    match eco_code:
        case "A40":
            return "Irregular Queen's Pawn Game (1. d4 ...)"
        case "B01":
            return "Scandinavian Defense (1. e4 d5)"
        case "C20":
            return "King's Pawn Game (1. e4 e5)"
        case "C50":
            return "Italian Game (1. e4 e5 2. Nf3 Nc6)"
        case "D00":
            return "Queen's Pawn Opening (1. d4 d5)"
        case "D02":
            return "London System (1. d4 d5 2. Nf3 Nf6 3. Bf4)"
        case "C21":
            return "Center Game (1. e4 e5 2. d4 exd4)"
        case "B06":
            return "Modern Defense (1. e4 g6)"
        case "C00":
            return "French Defense (1. e4 e6)"
        case "B00":
            return "Uncommon King's Pawn (1. e4 ...)"
        case "C41":
            return "Philidor Defense (1. e4 e5 2. Nf3 d6)"
        case "C42":
            return "Petrov's Defense (1. e4 e5 2. Nf3 Nf6)"
        case "C44":
            return "Scotch Game (1. e4 e5 2. Nf3 Nc6)"
        case "B10":
            return "Caro-Kann Defense (1. e4 c6)"
        case "A01":
            return "Nimzowitsch-Larsen Attack (1. b3 ...)"
        case "A04":
            return "Reti Opening (1. Nf3 ...)"
        case "C40":
            return "King's Knight Opening (1. e4 e5 2. Nf3 ...)"
        case "B20":
            return "Sicilian Defense (1. e4 c5)"
        case "C23":
            return "Bishop’s Opening (1. e4 e5 2. Bc4)"
        case "C01":
            return "French Defense (1. e4 e6 2. d4 d5)"
        case "A45":
            return "Queen's Pawn Opening (1. d4 Nf6)"
        case "D06":
            return "Queen's Gambit Declined (1. d4 d5 2. c4 Nf6)"
        case "D20":
            return "Queen's Gambit Accepted (1. d4 d5 2. c4 dxc4)"
        case "C25":
            return "Vienna Game (1. e4 e5 2. Nc3)"
        case "C30":
            return "King's Gambit (1. e4 e5 2. f4)"
        case "B40":
            return "Sicilian Defense (1. e4 c5 2. Nf3)"
        case "B13":
            return "Caro-Kann Defense: Exchange Variation (1. e4 c6 2. d4 d5 3. exd5 cxd5)"
        case "B21":
            return "Sicilian Defense: Smith-Morra Gambit (1. e4 c5 2. d4)"
        case "A06" :
            return "Zukertort Opening (1. Nf3)"
        case "C46" :
            return "Three Knights Game (1. e4 e5 2. Nf3 Nc6 3. Nc3)"
        case _:
            return eco_code  # fallback to just ECO code