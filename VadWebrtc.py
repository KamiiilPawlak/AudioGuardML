import  webrtcvad
import collections
import contextlib
import wave
import os

FRAME_DURATION = 30

def read_wave(path):
    with contextlib.closing(wave.open(path, 'rb')) as wf:
        assert wf.getnchannels() == 1
        assert wf.getsampwidth() == 2
        assert wf.getframerate() == 1600  
        pcm_data = wf.readframes(wf.getnframes())
        return pcm_data, wf.getframerate()

def frame_generator(frame_duration_ms, audio, sample_rate):
    n = int(sample_rate * (frame_duration_ms / 1000.0) * 2)
    offset = 0
    while offset + n <= len(audio):
        yield audio[offset:offset + n]
        offset += n
