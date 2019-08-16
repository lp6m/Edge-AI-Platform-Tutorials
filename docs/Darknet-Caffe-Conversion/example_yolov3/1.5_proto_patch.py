import os
import sys

argvs = sys.argv
argc = len(argvs)

if argc != 6:
    print 'Usage: # python %s prototxt yolo_height yolo_width calib_filelist_txt calib_img_dir'     % argvs[0]
    quit()
prototxt = argvs[1]
yolo_height = argvs[2]
yolo_width = argvs[3]
calib_filelist_txt = argvs[4]
calib_img_dir = argvs[5]

f = open(prototxt, 'r')
lines = f.readlines()
f.close()

template_for_decent_info = "layer {{\n" \
"  name: \"data\"\n" \
"  type: \"ImageData\"\n" \
"  top: \"data\"\n" \
"  top: \"label\"\n" \
"  include {{\n" \
"    phase: TRAIN\n" \
"  }}\n" \
"  transform_param {{\n" \
"    mirror: false\n" \
"    yolo_height:{0}  #change height according to Darknet model\n" \
"    yolo_width:{1}   #change width according to Darknet model\n" \
"  }}\n" \
"  image_data_param {{\n" \
"    source: \"{2}\"\n" \
"    root_folder: \"{3}\"\n" \
"\n" \
"    batch_size: 1\n" \
"    shuffle: false\n" \
"  }}\n" \
"}}\n" \
"\n".format(yolo_height, yolo_width, calib_filelist_txt, calib_img_dir)

f = open(prototxt, 'w')
phase = 0
for line in lines:
    if(phase == 0 and "input" in line):
        phase = 1
    if(phase == 1 and "layer" in line):
        f.write(template_for_decent_info)
        phase = 2
    if(phase == 1):
        line = "# " + line

    f.write(line)
f.close()
