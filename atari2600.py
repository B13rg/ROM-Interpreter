def interpretFile(indata, outfile):
	f = open(outfile, 'w+')

	for index in indata:
		line = opCodes(indata, index)
		f.write(line, '\n')
	f.close


def opCodes(indata, index):
    val = indata[index]

    if val == 0x0000:
    elif val == 0x0001:
    elif val == 0x0002:
        return "KIL"
    elif val == 0x0003:
    elif val == 0x0004:
    elif val == 0x0005:
    elif val == 0x0006:
    elif val == 0x0007:
    elif val == 0x0008:
	return "PHP	;[S]=P, S=S-1 (flags)"
    elif val == 0x0009:
    elif val == 0x000a:
	return "ASL A	;SHL A"
    elif val == 0x000b:
    elif val == 0x000c:
    elif val == 0x000d:
    elif val == 0x000e:
    elif val == 0x000f:
    elif val == 0x0010:
	
    elif val == 0x0011:
    elif val == 0x0012:
        return "KIL"
    elif val == 0x0013:
    elif val == 0x0014:
    elif val == 0x0015:
    elif val == 0x0016:
    elif val == 0x0017:
    elif val == 0x0018:
	return "CLC	;Clear carry flag"
    elif val == 0x0019:
    elif val == 0x001a:
        return "NOP"
    elif val == 0x001b:
    elif val == 0x001c:
    elif val == 0x001d:
    elif val == 0x001e:
    elif val == 0x001f:
    elif val == 0x0020:
    elif val == 0x0021:
    elif val == 0x0022:
        return "KIL"
    elif val == 0x0023:
    elif val == 0x0024:
        index ++
        return "BIT " + hex(indata[index]) + "    ;test and set flags"
    elif val == 0x0025:
    elif val == 0x0026:
    elif val == 0x0027:
    elif val == 0x0028:
	return "PLP	;S=S+1, P=[s] (flags)"
    elif val == 0x0029:
    elif val == 0x002a:
	return "ROL A	;RCL A"
    elif val == 0x002b:
    elif val == 0x002c:
	index ++
	val = hex(indata[index])
	index ++
	return "BIT " + val + hex(indata[index]) + "	;test and set flags" 
    elif val == 0x002d:
    elif val == 0x002e:
    elif val == 0x002f:
    elif val == 0x0030:
    elif val == 0x0031:
    elif val == 0x0032:
        return "KIL"
    elif val == 0x0033:
    elif val == 0x0034:
    elif val == 0x0035:
    elif val == 0x0036:
    elif val == 0x0037:
    elif val == 0x0038:
	return "SEC	;Set carry flag"
    elif val == 0x0039:
    elif val == 0x003a:
        return "NOP"
    elif val == 0x003b:
    elif val == 0x003c:
    elif val == 0x003d:
    elif val == 0x003e:
    elif val == 0x003f:
    elif val == 0x0040:
	return "RTI	;P=[S], PC=[S]"
    elif val == 0x0041:
    elif val == 0x0042:
        return "KIL"
    elif val == 0x0043:
    elif val == 0x0044:
    elif val == 0x0045:
    elif val == 0x0046:
    elif val == 0x0047:
    elif val == 0x0048:
	return "PHA	;[S]=A, S=S-1 PUSH"
    elif val == 0x0049:
    elif val == 0x004a:
	return "LSR A	;SHR A"
    elif val == 0x004b:
    elif val == 0x004c:
    elif val == 0x004d:
    elif val == 0x004e:
    elif val == 0x004f:
    elif val == 0x0050:
    elif val == 0x0051:
    elif val == 0x0052:
        return "KIL"
    elif val == 0x0053:
    elif val == 0x0054:
    elif val == 0x0055:
    elif val == 0x0056:
    elif val == 0x0057:
    elif val == 0x0058:
	return "CLI	;Clear interrupt disable bit"
    elif val == 0x0059:
    elif val == 0x005a:
        return "NOP"
    elif val == 0x005b:
    elif val == 0x005c:
    elif val == 0x005d:
    elif val == 0x005e:
    elif val == 0x005f:
    elif val == 0x0060:
	return "RTS	;PC=[S]+1"
    elif val == 0x0061:
    elif val == 0x0062:
        return "KIL"
    elif val == 0x0063:
    elif val == 0x0064: 
    elif val == 0x0065:
    elif val == 0x0066:
    elif val == 0x0067:
    elif val == 0x0068:
	return "PLA	;S=S+1, A=[S] POP"
    elif val == 0x0069:
    elif val == 0x006a:
	return "ROR A	;RCR A"
    elif val == 0x006b:
    elif val == 0x006c:
    elif val == 0x006d:
    elif val == 0x006e:
    elif val == 0x006f:
    elif val == 0x0070:
    elif val == 0x0071:
    elif val == 0x0072:
        return "KIL"
    elif val == 0x0073:
    elif val == 0x0074:
    elif val == 0x0075:
    elif val == 0x0076:
    elif val == 0x0077:
    elif val == 0x0078:
	return "SEI	;Set interrupt disable bit"
    elif val == 0x0079:
    elif val == 0x007a:
        return "NOP	;No operation"
    elif val == 0x007b:
    elif val == 0x007c:
    elif val == 0x007d:
    elif val == 0x007e:
    elif val == 0x007f:
    elif val == 0x0080:
    elif val == 0x0081:
    elif val == 0x0082:
    elif val == 0x0083:
    elif val == 0x0084:
    elif val == 0x0085:
    elif val == 0x0086:
    elif val == 0x0087:
    elif val == 0x0088:
	return "DEY	;Y = Y-1"
    elif val == 0x0089:
    elif val == 0x008a:
        return "TXA	;A=X"
    elif val == 0x008b:
    elif val == 0x008c:
    elif val == 0x008d:
    elif val == 0x008e:
    elif val == 0x008f:
    elif val == 0x0090:
    elif val == 0x0091:
    elif val == 0x0092:
        return "KIL"
    elif val == 0x0093:
    elif val == 0x0094:
    elif val == 0x0095:
    elif val == 0x0096:
    elif val == 0x0097:
    elif val == 0x0098:
        return "TYA	;A=Y"
    elif val == 0x0099:
    elif val == 0x009a:
        return "TXS	;S=Y"
    elif val == 0x009b:
    elif val == 0x009c:
    elif val == 0x009d:
    elif val == 0x009e:
    elif val == 0x009f:
    elif val == 0x00a0:
        index ++
        return "LDY #" + hex(indata[index]) + " ;Y=nn"
    elif val == 0x00a1:
    elif val == 0x00a2:
        index ++
        return "LDX #" + hex(indata[index]) + "    ;X=nn"
    elif val == 0x00a3:
    elif val == 0x00a4:
    elif val == 0x00a5:
        index ++
        return "LDA " + hex(indata[index]) + "  ;A=[nn]"
    elif val == 0x00a6:
    elif val == 0x00a7:
    elif val == 0x00a8:
        return "TAY ;Y=A"
    elif val == 0x00a9:
        index ++
        return "LDA #" + hex(indata[index]) + "   ;A=nn"
    elif val == 0x00aa:
        return "TAX ;X=A"
    elif val == 0x00ab:
    elif val == 0x00ac:
    elif val == 0x00ad:
        index ++
        byte = hex(indata[index])
        index ++
        return "LDA " + byte + hex(indata[index]) +  "  ;A=[nnnn]"
    elif val == 0x00ae:
    elif val == 0x00af:
    elif val == 0x00b0:
    elif val == 0x00b1:
    elif val == 0x00b2:
        return "KIL"
    elif val == 0x00b3:
    elif val == 0x00b4:
    elif val == 0x00b5:
        index ++
        return "LDA " + hex(indata[index]) + ",X    ;A==[nn+X]"
    elif val == 0x00b6:
    elif val == 0x00b7:
    elif val == 0x00b8:
	return "CLV	;Clear overflow flag"
    elif val == 0x00b9:
        index ++
        byte = hex(indata[index])
        index ++
        return "LDA " + byte + hex(indata[index]) +  ",Y   ;A=[nnnn+Y]"
    elif val == 0x00ba:
        return "TSX ;X=S"
    elif val == 0x00bb:
    elif val == 0x00bc:
    elif val == 0x00bd:
        index ++
        byte = hex(indata[index])
        index ++
        return "LDA " + byte + hex(indata[index]) +  ",X   ;A=[nnnn+X]"
    elif val == 0x00be:
    elif val == 0x00bf:
    elif val == 0x00c0:
    elif val == 0x00c1:
    elif val == 0x00c2:
    elif val == 0x00c3:
    elif val == 0x00c4:
    elif val == 0x00c5:
    elif val == 0x00c6:
    elif val == 0x00c7:
    elif val == 0x00c8:
	return "INY	;Y = Y+1"
    elif val == 0x00c9:
    elif val == 0x00ca:
	return "DEX	;X = X-1"
    elif val == 0x00cb:
    elif val == 0x00cc:
    elif val == 0x00cd:
    elif val == 0x00ce:
    elif val == 0x00cf:
    elif val == 0x00d0:
    elif val == 0x00d1:
    elif val == 0x00d2:
        return "KIL"
    elif val == 0x00d3:
    elif val == 0x00d4:
    elif val == 0x00d5:
    elif val == 0x00d6:
    elif val == 0x00d7:
    elif val == 0x00d8:
	return "CLD	;Clear decimal mode"
    elif val == 0x00d9:
    elif val == 0x00da:
	return "NOP	;No operation"
    elif val == 0x00db:
    elif val == 0x00dc:
    elif val == 0x00dd:
    elif val == 0x00de:
    elif val == 0x00df:
    elif val == 0x00e0:
    elif val == 0x00e1:
    elif val == 0x00e2:
    elif val == 0x00e3:
    elif val == 0x00e4:
    elif val == 0x00e5:
    elif val == 0x00e6:
    elif val == 0x00e7:
    elif val == 0x00e8:
	return "INX	;X = X+1"
    elif val == 0x00e9:
    elif val == 0x00ea:
	return "NOP	;No operation"
    elif val == 0x00eb:
    elif val == 0x00ec:
    elif val == 0x00ed:
    elif val == 0x00ee:
    elif val == 0x00ef:
    elif val == 0x00f0:
    elif val == 0x00f1:
    elif val == 0x00f2:
        return "KIL"
    elif val == 0x00f3:
    elif val == 0x00f4:
    elif val == 0x00f5:
    elif val == 0x00f6:
    elif val == 0x00f7:
    elif val == 0x00f8:
	return "SED	;Set decimel mode"
    elif val == 0x00f9:
    elif val == 0x00fa:
	return "NOP	;No operation"
    elif val == 0x00fb:
    elif val == 0x00fc:
    elif val == 0x00fd:
    elif val == 0x00fe:
    elif val == 0x00ff:

