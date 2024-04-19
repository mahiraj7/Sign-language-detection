def check_yes_sign(hand_landmarks, hand_type):
    is_thumb_yes_position_correct = check_yes_sign_thumb(hand_landmarks, hand_type)
    is_index_yes_position_correct = check_yes_sign_index(hand_landmarks)
    is_middle_yes_position_correct = check_yes_sign_middle(hand_landmarks)
    is_ring_yes_position_correct = check_yes_sign_ring(hand_landmarks)
    is_little_yes_position_correct = check_yes_sign_little(hand_landmarks)
    return is_thumb_yes_position_correct and is_index_yes_position_correct and is_middle_yes_position_correct and is_ring_yes_position_correct and is_little_yes_position_correct

def check_yes_sign_thumb(hand_landmarks, hand_type):
    result = False
    if hand_type == 'right':
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[0].x and hand_landmarks.landmark[3].x > hand_landmarks.landmark[1].x:
            result = True
    elif hand_type == 'left':
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[0].x and hand_landmarks.landmark[3].x < hand_landmarks.landmark[1].x:
            result = True
			
    return result

def check_yes_sign_index(hand_landmarks):			
    return hand_landmarks.landmark[8].y > hand_landmarks.landmark[6].y

def check_yes_sign_middle(hand_landmarks):			
    return hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y

def check_yes_sign_ring(hand_landmarks):
    return hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y

def check_yes_sign_little(hand_landmarks):
    return hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y

