from main import Iec104

print('=' * 50)
print(f'type 0x0D (13). IEEE STD 754 QDS')
telegram = Iec104('68 17 A8 00 04 00 0D 82 01 57 57 00 E7 0B 00 0A D7 A3 BB 00 7F 6A BC 3C 00')
telegram.report()

print('=' * 50)
print(f'type 0x1E (30). SIQ CP56Time2a')
telegram = Iec104('68 15 42 EB D2 01 1E 01 03 00 80 00 B0 36 00 01 AF E1 1D 14 70 06 15')
telegram.report()

print('=' * 50)
print(f'type 0x22 (34). NVA QDS CP56Time2a')
telegram = Iec104('68 17 BA 8C F2 00 22 01 01 00 03 00 01 00 00 01 00 00 08 7F 0E 09 96 04 15')
telegram.report()

print('=' * 50)
print(f'type 0x24 (36). IEEE STD 754 QDS CP56Time2a')
telegram = Iec104('68 19 FE 08 30 01 24 01 03 51 51 00 EE 03 00 4B E7 47 42 00 91 05 32 0A 69 06 15')
telegram.report()

print('=' * 50)
print(f'type 0x64 (100). GI activation')
telegram = Iec104('68 0E 00 00 04 00 64 01 06 00 71 00 00 00 00 14')
telegram.report()

print('=' * 50)
print(f'type 0x64 (100). GI confirmation')
telegram = Iec104('68 0E 04 00 02 00 64 01 07 71 71 00 00 00 00 14')
telegram.report()
