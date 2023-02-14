import os
import numpy as np
import pyaudio

import extract_feats.opensmile as of
import extract_feats.librosa as lf
import models
import utils
import wave
import soundfile as sf

def predict(config, audio_path: str, model) -> None:
    """
    预测音频情感

    Args:
        config: 配置项
        audio_path (str): 要预测的音频路径
        model: 加载的模型
    """

    #utils.play_audio(audio_path)

    if config.feature_method == 'o':
        # 一个玄学 bug 的暂时性解决方案
        of.get_data(config, audio_path, train=False)
        test_feature = of.load_feature(config, train=False)
    elif config.feature_method == 'l':
        test_feature = lf.get_data(config, audio_path, train=False)

    result = model.predict(test_feature)
    result_prob = model.predict_proba(test_feature)
    print('Recogntion: ', config.class_labels[int(result)])
    print('Probability: ', result_prob)
    utils.radar(result_prob, config.class_labels)

def record():
    # 定义数据流块
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    # 想要百度识别，下面这两参数必须这样设置，使得比特率为256kbps
    CHANNELS = 1
    RATE = 16000
    # 录音时间
    RECORD_SECONDS = 8
    # 要写入的文件名
    WAVE_OUTPUT_FILENAME = "input.wav"
    # 创建PyAudio对象
    p = pyaudio.PyAudio()

    # 打开数据流
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    # 开始录音
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")
    # 停止数据流
    stream.stop_stream()
    stream.close()

    # 关闭PyAudio
    p.terminate()

    # 写入录音文件
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    #record()
    #audio_path = 'G:\Ruabit\Speech-Emotion-Recognition-master\input.wav'
    audio_path = 'G:\\Ruabit\\Speech-Emotion-Recognition-master\\datasets\\surprise\\03-01-08-01-01-01-01.wav'
    config = utils.parse_opt()
    model = models.load(config)
    predict(config, audio_path, model)
