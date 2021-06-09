#!/usr/bin/env python3

########################################################################################################################
# Author: Suat Gedikli
# Copyright Suat Gedikli 2021
########################################################################################################################


import argparse
import math
import os
import time
from PIL import Image

DelTag16h5 = [0x231b, 0x2ea5, 0x346a, 0x45b9, 0x79a6, 0x7f6b, 0xb358, 0xe745, 0xfe59, 0x156d,
              0x380b, 0xf0ab, 0x0d84, 0x4736, 0x8c72, 0xaf10, 0x093c, 0x93b4, 0xa503, 0x468f,
              0xe137, 0x5795, 0xdf42, 0x1c1d, 0xe9dc, 0x73ad, 0xad5f, 0xd530, 0x07ca, 0xaf2e]

DelTag25h7 = [0x04b770d, 0x11693e6, 0x1a599ab, 0x0c3a535, 0x152aafa, 0x0Accd98, 0x1cad922, 0x02c2fad, 0x0Bb3572,
              0x14a3b37, 0x186524b, 0x0c99d4c, 0x023bfea, 0x141cb74, 0x1d0d139, 0x1670aeb, 0x0851675, 0x150334e,
              0x06e3ed8, 0x0Fd449d, 0x1d6c950, 0x08b0e8c, 0x11a1451, 0x1562b65, 0x13f53c8, 0x0D58d7a, 0x0829ec9,
              0x0Faccf1, 0x136e405, 0x07a2f06, 0x10934cb, 0x16a8b56, 0x1a6a26a, 0x0F85545, 0x195c2e4, 0x024c8a9,
              0x12bfc96, 0x16813aa, 0x1a42abe, 0x1573424, 0x1044573, 0x0B156c2, 0x05e6811, 0x1659bfe, 0x1d55a63,
              0x05bf065, 0x0E28667, 0x1e9ba54, 0x17d7c5a, 0x1f5aa82, 0x1a2bbd1, 0x01ae9f9, 0x1259e51, 0x134062b,
              0x0e1177a, 0x0Ed07a8, 0x162be24, 0x059128b, 0x1663e8f, 0x01a83cb, 0x045bb59, 0x189065a, 0x04bb370,
              0x16fb711, 0x122c077, 0x0Eca17a, 0x0Dbc1f4, 0x088d343, 0x058ac5d, 0x0Ba02e8, 0x01a1d9d, 0x1c72eec,
              0x0924bc5, 0x0Dccab3, 0x0886d15, 0x178c965, 0x05bc69a, 0x1716261, 0x174e2cc, 0x1ed10f4, 0x0156aa8,
              0x03e2a8a, 0x02752ed, 0x153c651, 0x1741670, 0x0765b05, 0x119c0bb, 0x172a783, 0x04faca1, 0x0F31257,
              0x12441fc, 0x00d3748, 0x0c21f15, 0x0Ac5037, 0x180e592, 0x07d3210, 0x0A27187, 0x02beeaf, 0x026ff57,
              0x0690e82, 0x077765c, 0x1a9e1d7, 0x140be1a, 0x1aa1e3a, 0x1944f5c, 0x19b5032, 0x0169897, 0x1068eb9,
              0x0f30dbc, 0x106a151, 0x1d53e95, 0x1348cee, 0x0cf4fca, 0x1728bb5, 0x0Dc1eec, 0x069e8db, 0x16e1523,
              0x105fa25, 0x18abb0c, 0x0c4275d, 0x06d8e76, 0x0E8d6db, 0x0E16fd7, 0x1ac2682, 0x077435b, 0x0A359dd,
              0x03a9c4e, 0x123919a, 0x1e25817, 0x002a836, 0x01545a4, 0x1209c8d, 0x0Bb5f69, 0x1dc1f02, 0x05d5f7e,
              0x12d0581, 0x13786c2, 0x0E15409, 0x1aa3599, 0x139aad8, 0x0B09d2a, 0x054488f, 0x13c351c, 0x0976079,
              0x0b25b12, 0x1addb34, 0x1cb23ae, 0x1175738, 0x1303bb8, 0x0D47716, 0x188ceea, 0x0Baf967, 0x1226d39,
              0x135e99b, 0x034adc5, 0x02e384d, 0x090d3fa, 0x0232713, 0x17d49b1, 0x0Aa84d6, 0x0c2ddf8, 0x1665646,
              0x04f345f, 0x02276b1, 0x1255dd7, 0x16f4ccc, 0x04aaffc, 0x0c46da6, 0x085c7b3, 0x1311fcb, 0x09c6c4f,
              0x187d947, 0x08578e4, 0x0E2bf0b, 0x0A01b4c, 0x0A1493b, 0x07ad766, 0x0ccfe82, 0x1981b5b, 0x1cacc85,
              0x0562cdb, 0x15b0e78, 0x08f66c5, 0x03332bf, 0x12ce754, 0x0096a76, 0x1d5e3ba, 0x027ea41, 0x14412df,
              0x067b9b4, 0x0Daa51a, 0x01dcb17, 0x04d4afd, 0x06335d5, 0x0Ee2334, 0x17d4e55, 0x1b8b0f0, 0x14999e3,
              0x1513dfa, 0x0765cf2, 0x056af90, 0x12e16ac, 0x1d3d86c, 0x0Ff279b, 0x18822dd, 0x099d478, 0x08dc0d2,
              0x034b666, 0x0cf9526, 0x186443d, 0x07a8e29, 0x19c6aa5, 0x1f2a27d, 0x12b2136, 0x0D0cd0d, 0x12cb320,
              0x17ddb0b, 0x005353b, 0x15b2caf, 0x1e5a507, 0x120f1e5, 0x114605a, 0x14efe4c, 0x0568134, 0x11b9f92,
              0x174d2a7, 0x0692b1d, 0x039e4fe, 0x0Aaff3d, 0x096224c, 0x13c9f77, 0x110ee8f, 0x0F17bea, 0x099fb5d,
              0x0337141, 0x002b54d, 0x1233a70]

DelTag25h9 = [0x155cbf1, 0x1e4d1b6, 0x17b0b68, 0x1eac9cd, 0x12e14ce, 0x03548bb, 0x07757e6,
              0x1065dab, 0x1baa2e7, 0x0dea688, 0x081d927, 0x051b241, 0x0dbc8ae, 0x1e50e19,
              0x15819d2, 0x16d8282, 0x163e035, 0x09d9b81, 0x173eec4, 0x0ae3a09, 0x05f7c51,
              0x1a137fc, 0x0dc9562, 0x1802e45, 0x1c3542c, 0x0870fa4, 0x0914709, 0x16684f0,
              0x0c8f2a5, 0x0833ebb, 0x059717f, 0x13cd050, 0x0fa0ad1, 0x1b763b0, 0x0b991ce]

HEIGHT = math.sqrt(3.0) * 0.5


def generate_dsc(output, cols, size, skip, tag_name, tag_start, board_id):
    output.write("%d , %d , 0 , %f\n" % (board_id, cols, size))  # board.id, lx, ly, size
    output.write("%s,1.0\n" % tag_name)  # tag family
    dx = size
    dy = size * math.sqrt(3.0) * 0.5
    x = 0.0
    y = 0.0
    cur_id = tag_start
    for row in range(cols - 2):
        x = 0.5 * dx * row
        for col in range(cols - 2 - row):
            tag_id = -1
            if tag_name != 'none' and row % skip == 0 and col % skip == 0:
                tag_id = cur_id
                cur_id += 1
            output.write("%3d , %2d , %2d , %3.15f , %3.15f , 0.000\n" % (tag_id, col, row, x, y))
            x += dx
        y += dy


def generate_DelTag(output, tag_id, tag_dim, codes):
    scale = tag_dim + 3
    output.write("gsave\n")
    output.write("%2.8f %2.8f scale\n" % (1.0 / (tag_dim + 3), 1.0 / (tag_dim + 3)))
    output.write("newpath\n")
    output.write("0 0 moveto\n")
    output.write("%2.8f 0 lineto\n" % scale)
    output.write("%2.8f %2.8f lineto\n" % (scale * 0.5, HEIGHT * scale))
    output.write("closepath\n")
    output.write("%2.8f %2.8f moveto\n" % (1.5, HEIGHT))
    output.write("%2.8f %2.8f lineto\n" % (scale * 0.5, HEIGHT * (scale - 2)))
    output.write("%2.8f %2.8f lineto\n" % ((scale - 1.5), HEIGHT))
    output.write("closepath\n")
    # output.write("0.5 0.5 0.5 setrgbcolor\n")
    output.write("fill\n")
    output.write("%2.8f %2.8f translate\n" % (1.0 + 0.5 * tag_dim, tag_dim * HEIGHT))
    # output.write("0 0 0 setrgbcolor\n")
    code = codes[tag_id]
    for bitrow in range(tag_dim):
        output.write("gsave\n")
        for bitcol in range(2 * bitrow + 1):
            bit = tag_dim * tag_dim - (bitrow * bitrow + bitcol) - 1
            if code & (1 << bit) == 0:
                if bitcol % 2 == 0:
                    output.write("lowerTri\n")
                else:
                    output.write("upperTri\n")
            if bitcol % 2 == 0:
                output.write("1 0 translate\n")
        output.write("grestore\n")
        output.write("-0.5 %2.8f translate\n" % (-HEIGHT))
    output.write("grestore\n")


def generate_pattern(basename, cols, size, skip, tag_name, transparent, tag_start, board_id):
    ps_filename = basename + '.ps'
    corners_filename = basename + '.csv'
    ppi = 72  # ppi for postscript coordinate frame
    inch2mm = 25.4  # conversion of 1 inch to cm
    ppmm = ppi / inch2mm  # point per cm
    border = 1.0  # in size of triangles
    resolution = 360.0  # dpi for the png file to be created with this ps file

    # calculate a paper size that fits
    pattern_width = cols * size
    pattern_height = cols * HEIGHT * size
    paper_width = pattern_width + 2 * border * size
    paper_height = pattern_height + 2 * border * size * HEIGHT
    if paper_width > paper_height:
        paper_height = paper_width
    else:
        paper_width = paper_height

    with open(ps_filename, "w") as output, open(corners_filename, "w") as corners:
        output.write("%!PS-Adobe-2.0 EPSF-2.0\n")
        output.write("%%%%BoundingBox: 0 0 %d %d\n\n" % (int(paper_width * ppmm), int(paper_height * ppmm)))
        output.write("%%Title: Deltille Pattern and Tags\n\n")
        output.write("<</PageSize [ %d %d ]>> setpagedevice\n" %
                     (int(paper_width * ppmm + 0.5), int(paper_height * ppmm + 0.5)))
        output.write("/lowerTri {\n")
        output.write("        gsave\n")
        output.write("        newpath\n")
        output.write("        0 0 moveto\n")
        output.write("        1 0 lineto\n")
        output.write("        0.5 %2.8f lineto\n" % HEIGHT)
        output.write("        closepath\n")
        output.write("        fill\n")
        output.write("        grestore\n")
        output.write("} def\n\n")
        output.write("/upperTri {\n")
        output.write("        gsave\n")
        output.write("        newpath\n")
        output.write("        0 0 moveto\n")
        output.write("        -0.5 %2.8f lineto\n" % HEIGHT)
        output.write("        +0.5 %2.8f lineto\n" % HEIGHT)
        output.write("        closepath\n")
        output.write("        fill\n")
        output.write("        grestore\n")
        output.write("} def\n\n")
        output.write("%2.8f %2.8f scale\n" % (size * ppmm, size * ppmm))
        output.write("gsave\n")
        output.write("%f %f translate\n" % (border, border))

        corners.write("1, %d, %f\n" % (board_id, resolution))
        corners.write("3, %4.15f, %4.15f, %4.15f, %4.15f, %4.15f, %4.15f\n" %
                      (border * size * resolution / inch2mm,
                       (paper_height - border * size) * resolution / inch2mm,
                       (cols / 2 + border) * size * resolution / inch2mm,
                       (paper_height - (cols * HEIGHT + border) * size) * resolution / inch2mm,
                       (cols + border) * size * resolution / inch2mm,
                       (paper_height - border * size) * resolution / inch2mm
                       ))
        # print the outline of the whole pattern
        y = 0.0
        tag_id = tag_start
        tags = []
        for row in range(cols):
            x = 0.5 * row
            output.write("gsave\n")
            for col in range(cols - row):
                if row % skip == 1 and col % skip == 1:
                    if tag_name == 't25h7':
                        generate_DelTag(output, tag_id, 5, DelTag25h7)
                        tags.append(DelTag16h5[tag_id])
                        tag_id += 1
                    elif tag_name == 't25h9':
                        generate_DelTag(output, tag_id, 5, DelTag25h9)
                        tags.append(DelTag25h9[tag_id])
                        tag_id += 1
                    elif tag_name == 't16h5':
                        generate_DelTag(output, tag_id, 4, DelTag16h5)
                        tags.append(DelTag16h5[tag_id])
                        tag_id += 1
                    else:
                        output.write("lowerTri\n")
                else:
                    output.write("lowerTri\n")

                x_cm = (x + border) * size
                y_cm = paper_height - (y + border) * size
                print("%f %f -> %4.3f %4.3f -> %4.3f %4.3f" % (x, y, x_cm, y_cm, x_cm * resolution / inch2mm,
                                                               y_cm * resolution / inch2mm))
                if col > 0 and row > 0:
                    corner_id = (row - 1) * (cols - 2) + (col - 1)
                    corners.write("%d, %d, %d, %4.15f, %4.15f\n" % (row, col, corner_id, x_cm * resolution / inch2mm -0.5,
                                                            y_cm * resolution / inch2mm -0.5))
                output.write("1 0 translate\n")
                x += 1
            output.write("grestore\n")

            y += HEIGHT
            output.write("0.5 %2.8f translate\n" % HEIGHT)
        output.write("grestore\n")
        output.write("/Courier findfont\n0.2 scalefont\n setfont\n")
        output.write("%f %f moveto\n" % (border - 0.5, border - 0.5))
        output.write("(Deltille, %dx%d, %1.2fcm, #%d, %s:" % (cols, cols, size, board_id, tag_name))
        for tag in tags:
            output.write(" %s" % hex(tag))
        output.write(") false charpath\n")
        output.write(".0025 setlinewidth\nstroke\n")
        output.write("showpage\n\n")

    while not os.path.exists(ps_filename):
        print("waiting for ps file...")
        time.sleep(1)
    print("generating png file...")
    png_filename = basename + '.png'
    cmd = ""
    if transparent:
        cmd = "gs -dSAFER -dBATCH -dNOPAUSE -dEPSCrop -r%d -sDEVICE=pngalpha -sOutputFile=%s %s" % \
              (resolution, png_filename, ps_filename)
    else:
        cmd = "gs -dSAFER -dBATCH -dNOPAUSE -dEPSCrop -r%d -sDEVICE=pnggray -dGraphicsAlphaBits=4 -sOutputFile=%s %s" % \
              (resolution, png_filename, ps_filename)

    os.system(cmd)


def main():
    parser = argparse.ArgumentParser(description="generate dsc file for triangular pattern")
    #    parser.add_argument('--rows', type=int,
    #                        help="number of triangle rows",
    #                        required=True)
    parser.add_argument('--cols',
                        type=int,
                        help="number of triangle cols. Must be even if DelTags are used.",
                        required=True)
    parser.add_argument('--size',
                        type=float,
                        default=2.0,
                        help="size of triangle side",
                        required=False)
    parser.add_argument('--skip',
                        type=int,
                        default=2,
                        help="how many triangles to skip for each tag",
                        required=False)
    parser.add_argument('--tag_name',
                        type=str,
                        default="t16h5",
                        help="name of the tag family. Only 'none', 't16h5', 't25h7' and 't25h9' are supported.",
                        required=False)
    parser.add_argument('--transparent',
                        type=bool,
                        default=False,
                        required=False)
    parser.add_argument('--output',
                        type=str,
                        default="",
                        help="filename for output dsc file",
                        required=False)
    parser.add_argument('--boardId',
                        type=int,
                        default="0",
                        help="which board to generate. Default 0, -1 = all.",
                        required=False)
    args = parser.parse_args()

    if args.tag_name != "none" and (args.cols % 2) != 0:
        print("please use an even number of columns when using Deltags")
        exit(1)

    if args.tag_name != "none" and args.tag_name != "t16h5" and args.tag_name != 't25h7' and args.tag_name != 't25h9':
        print("Only tag_name 'none', 't16h5', 't25h7' and 't25h9' are supported for now.")
        exit(1)

    basename = args.output;
    if basename == "":
        basename = "Deltille_%02d_%2.2f_%s_" % (args.cols, args.size, args.tag_name)

    tags_per_row = int((args.cols - 4) / args.skip) + 1
    tags_per_board = int(((tags_per_row + 1) * tags_per_row) / 2)
    #print("================= ", tags_per_row, tags_per_board)
    #tags_per_board = int(((args.cols / 2 - 1) * (args.cols / 2)) / 2)

    max_boards = int(len(DelTag16h5) / tags_per_board)
    if args.tag_name == "t25h7":
        max_boards = len(DelTag25h7) / tags_per_board
    elif args.tag_name == "t25h9":
        max_boards = len(DelTag25h9) / tags_per_board

    print(tags_per_board, max_boards)

    if args.boardId == -1:
        dsc_file = open(basename + "all.dsc", "w")
        for board_id in range(max_boards):
            filename = basename + str(board_id)
            print(dsc_file.closed)
            generate_dsc(dsc_file, args.cols, args.size, args.skip, args.tag_name, int(board_id * tags_per_board), board_id)
            generate_pattern(filename, args.cols, args.size, args.skip, args.tag_name, args.transparent,
                             int(board_id * tags_per_board), board_id)
    elif args.boardId < 0 or args.boardId > max_boards:
        print("board id exceeds number of possible boards for tag %s. It must be in the range [0, %2d]" %
              (args.tag_name, max_boards))
        exit(1)
    else:
        filename = basename + str(args.boardId)
        dsc_file = open(filename + ".dsc", "w")
        generate_dsc(dsc_file, args.cols, args.size, args.skip, args.tag_name, int(args.boardId * tags_per_board), args.boardId)
        generate_pattern(filename, args.cols, args.size, args.skip, args.tag_name, args.transparent,
                         int(args.boardId * tags_per_board), args.boardId)


if __name__ == "__main__":
    main()
