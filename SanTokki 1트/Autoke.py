from re import split
import matplotlib.pyplot as plt

from swift_f0 import *



# 1. 디텍터 설정

# 말씀하신 대로 0.9는 매우 높아서 소리가 조금만 흐릿해도 무시될 수 있습니다.

# 0.8 정도로 낮추신 건 아주 좋은 선택입니다!

detector = SwiftF0(fmin=120, fmax=1000, confidence_threshold=0.6)



# 2. 오디오 파일 경로 (문법 오류 수정)

# 경로 앞에 r을 붙여서 역슬래시 문제를 해결했습니다.

audio_path = r".\SanTokki_Vocal.mp3"



# 3. 피치 검출 실행

result = detector.detect_from_file(audio_path)



# 4. 결과 시각화 및 CSV 저장

# show=False로 하면 창이 뜨지 않고 파일로만 저장됩니다.

plot_pitch(result, show=False, output_path="Tokki_pitch.jpg")

export_to_csv(result, "Tokki_pitch_data.csv")



# 5. 음표 단위 분할 (Segmentation)

notes = segment_notes(

    result,
    #1.5 반음 이상 변해야 새 음으로 인식
    split_semitone_threshold=1.5,
    #음표 단위 분할: 기준을 넉넉하게 잡아서 음이 쪼개지는 걸 막음
    min_note_duration=0.089

)



# 6. 추가 시각화 및 MIDI 내보내기

plot_notes(notes, output_path="note_segments.jpg")

plot_pitch_and_notes(result, notes, output_path="combined_analysis.jpg")

export_to_midi(notes, "notes.mid")



print("모든 분석 파일(jpg, csv, mid)이 저장되었습니다.")