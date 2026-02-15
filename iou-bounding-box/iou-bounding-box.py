def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    x1a, y1a, x2a, y2a = box_a
    x1b, y1b, x2b, y2b = box_b

    area_a = (x2a - x1a) * (y2a - y1a)
    area_b = (x2b - x1b) * (y2b - y1b)

    inter_x1 = max(x1a, x1b)
    inter_y1 = max(y1a, y1b)
    inter_x2 = min(x2a, x2b)
    inter_y2 = min(y2a, y2b)

    inter_w = max(0.0, inter_x2 - inter_x1)
    inter_h = max(0.0, inter_y2 - inter_y1)

    intersection = inter_w * inter_h
    union = area_a + area_b - intersection

    if union == 0:
        return 0.0

    return intersection / union