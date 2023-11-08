import cv2

# RTSP URL
rtsp_url = 'rtsp://your_rtsp_stream_url'

# Open RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Initialize frame counter
frame_count = 0

# Loop through frames
while True:
    # Read frame
    ret, frame = cap.read()

    # If frame is read correctly
    if ret:
        # Increment frame counter
        frame_count += 1

        # If it's the 30th frame
        if frame_count % 30 == 0:
            # Save frame as image
            cv2.imwrite(f'frame_{frame_count}.jpg', frame)

        # Display frame
        cv2.imshow('frame', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
