import wave,struct,math

sampleRate = 44100.0 #hertz
duration = 10 #seconds
frequency = 440.0 #hertz

wavef = wave.open('sound.wav' , 'w')
wavef.setnchannels(2) # mono , 2 for stereo
wavef.setsampwidth(2)
wavef.setframerate(sampleRate) #44100 samples per second , mmm kay

for i in range(int(duration * sampleRate)):
    l = int(-32767.0*math.cos(300*math.pi*float(i)/float(sampleRate)))
    r = int(-32767.0*math.cos(1000*math.pi*float(i)/float(sampleRate)))
    data = struct.pack('<hh', l , r)
    wavef.writeframesraw(data)

wavef.writeframes('')
wavef.close()