def check_no_sign(hand_landmarks, hand_type):
    is_thumb_position_correct = check_no_sign_thumb(hand_landmarks, hand_type)
    is_index_position_correct = check_no_sign_index(hand_landmarks)
    is_middle_position_correct = check_no_sign_middle(hand_landmarks)
    is_ring_position_correct = check_no_sign_ring(hand_landmarks)
    is_little_position_correct = check_no_sign_little(hand_landmarks)
    return is_thumb_position_correct and is_index_position_correct and is_middle_position_correct and is_ring_position_correct and is_little_position_correct

def check_no_sign_thumb(hand_landmarks, hand_type):
    result = False
    if hand_type == 'right':
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            result = True
    elif hand_type == 'left':
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            result = True
			
    return result

def check_no_sign_index(hand_landmarks):			
    return hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y

def check_no_sign_middle(hand_landmarks):			
    return hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y

def check_no_sign_ring(hand_landmarks):
    return hand_landmarks.landmark[13].y < hand_landmarks.landmark[16].y

def check_no_sign_little(hand_landmarks):
    return hand_landmarks.landmark[17].y < hand_landmarks.landmark[20].y

