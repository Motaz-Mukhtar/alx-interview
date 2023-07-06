#!usr/bin/python3
"""
  Lock Boxes
"""


def canUnlockAll(boxes):
	"""
	Determine if all the boxes
	can opened.
	"""
	opened_boxes = []
	opened_boxes.appendboxes[0])

	if boxes[0] == []:
		return False

	for box in opened_boxes:
		for key in box:
			if boxes[key] in opened_boxes:
				continue
			opened_boxes.append(boxes[key])
	if len(boxes) == len(opened_boxes):
		return True
	else:
		return False
