#!/usr/bin/env python

import os
import numpy as np
import pylab as py
import healpy as H
from matplotlib import colors
import matplotlib.cm as cm


def plotArea(area_x, area_y):
    for i in range(len(area_x)):
        if len(area_x[i]) > 1:
            x1 = np.linspace(area_x[i][0], area_x[i][1], 100)  # np.arange(-100,110,10)
        else:
            x1 = np.zeros(100) + area_x[i]

        if len(area_y[i]) > 1:
            y1 = np.linspace(area_y[i][0], area_y[i][1], 100)  # np.arange(-100,110,10)
        else:
            y1 = np.zeros(100) + area_y[i]

        H.projplot((90. - x1) * np.pi / 180., y1 * np.pi / 180., 'g', lw=2.)  # ,rot=(0,-90,90),coord=['G','E'])


################################################################################

def main():
    _path = os.path.dirname(os.path.abspath(__file__))

    file_area = ['data/dcorr_smpas_obstime_15.fits', 'data/lambda_sfd_ebv.fits']

    splus_tilles = os.path.join(_path,'data/splus_tiles.txt')
    sn_tiles_file = '/Users/tiago/OneDrive/Documents/Documents/t80s/s-plus/sn2.txt'
    #
    # Reading data
    #

    map_area = np.array([H.read_map(os.path.join(_path, file_area[0])), ])
    pt_splus = np.loadtxt(splus_tilles, unpack=True, usecols=(1, 2))
    sn_tiles = np.loadtxt(sn_tiles_file, unpack=True)

    for i in range(1, len(file_area)):
        map_area = np.append(map_area, np.array([H.read_map(os.path.join(_path, file_area[i])), ]), axis=0)

    #
    # Plotting graph
    #

    # H.cartview(map_area[0], coord=['G', 'E'], cmap=cm.gray_r, cbar=False, notext=True,
    #            title='S-PLUS Survey Area') #, max=1)

    H.cartview(map_area[0], coord=['G', 'C'], cmap=cm.gray_r, cbar=False, notext=True,
               title='S-PLUS Survey Area') #, max=1)

    ####################################################################################################################
    # START S-PLUS

    #
    # S-PLUS Southern part
    #

    # for line in np.arange(-5, 1, 0.25):
    #     # dec = np.zeros(100)+(90+20*np.sin(line))*np.pi/180.
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(35, -35, 100)) * np.pi / 180., '-',
    #                color='b', lw=1, alpha=0.2)
    for line in np.arange(15, 45, 0.25):
        # H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(1, -35, 100)) * np.pi / 180., '-',
        #            color='m', lw=1) #, alpha=0.2)
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(60., -60, 100)) * np.pi / 180., '-',
                   color='r', lw=1, alpha=0.2)

    for line in np.arange(45, 75, 0.25):
        # H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(1, -35, 100)) * np.pi / 180., '-',
        #            color='m', lw=1) #, alpha=0.2)
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(70., -70, 100)) * np.pi / 180., '-',
                   color='r', lw=1, alpha=0.2)

    ######
    # for line in np.arange(15, 35, 0.25):
    #     # H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(1, -35, 100)) * np.pi / 180., '-',
    #     #            color='m', lw=1) #, alpha=0.2)
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(0., -30, 100)) * np.pi / 180., '-',
    #                color='r', lw=1, alpha=0.2)
    # for line in np.arange(35, 55, 0.25):
    #     # H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(1, -35, 100)) * np.pi / 180., '-',
    #     #            color='m', lw=1) #, alpha=0.2)
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(0., -60, 100)) * np.pi / 180., '-',
    #                color='r', lw=1, alpha=0.2)
    # for line in np.arange(20, 55, 0.25):
    #     # H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(1, -35, 100)) * np.pi / 180., '-',
    #     #            color='m', lw=1) #, alpha=0.2)
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(0., 22.5, 100)) * np.pi / 180., '-',
    #                color='r', lw=1, alpha=0.2)
    # for line in np.arange(20, 60, 0.25):
    #     # H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(1, -35, 100)) * np.pi / 180., '-',
    #     #            color='m', lw=1) #, alpha=0.2)
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(22.5, 60, 100)) * np.pi / 180., '-',
    #                color='r', lw=1, alpha=0.2)
    ######

    # for line in np.arange(15, 60, 0.25):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(45, -75, 100)) * np.pi / 180., '-',
    #                color='r', lw=1, alpha=0.2)

    # for line in np.arange(30, 60, 0.25):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(40, -60, 100)) * np.pi / 180., '-',
    #                color='r', lw=1, alpha=0.2)

    # for line in np.arange(60, 80, 0.25):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(80, -80, 100)) * np.pi / 180., '-',
    #                color='r', lw=1, alpha=0.2)

    # ra = np.linspace(-180*np.pi/180.,-150*np.pi/180.,100.)
    # dec = np.zeros(100)+(90+20*np.sin(ra))*np.pi/180.
    # for line in np.arange(-4.,4.,0.25):
    #     H.projplot(dec+line * np.pi/180.,ra,'-',color='m',lw=2.)
    #
    # ra = np.linspace(150*np.pi/180.,180*np.pi/180.,100.)
    # dec = np.zeros(100)+(90+20*np.sin(ra))*np.pi/180.
    # for line in np.arange(-4.,4.,0.25):
    #     H.projplot(dec+line * np.pi/180.,ra,'-',color='m',lw=2.)

    # for ra in np.linspace(-35 * np.pi / 180.,35 * np.pi / 180.,30.):
    #     dec = (90+20*np.sin(ra))*np.pi/180.
    #     H.projplot(np.array([dec, dec]) - 10. * np.pi / 180. ,[ra, -35 * np.pi /180.]  ,'-',color='r',lw=2.,alpha=0.2)
    # for line in np.arange(dec[0], dec[-1] , 0.25):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-35, 35, 100)) * np.pi / 180., '-',
    #                color='r', lw=1, alpha=0.2)

    # for line in np.arange(30, 45, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-60, 91, 100)) * np.pi / 180., '-',
    #                color='r', lw=2, alpha=0.9)
    # for line in np.arange(45, 80, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-90, 90, 100)) * np.pi / 180., '-',
    #                color='r', lw=2, alpha=0.9)

    #
    # S-PLUS Northern part
    #
    for line in np.arange(-10, 40, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(150, 180, 100)) * np.pi / 180., '-',
                   color='r', lw=2, alpha=0.2)
        # H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-157.5, -180, 100)) * np.pi / 180., '-',
        #            color='r', lw=2, alpha=0.2)
    # for line in np.arange(-15, 0, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(157.5,180, 100)) * np.pi / 180., '-',
    #                color='r', lw=2, alpha=0.9)

    # for line in np.arange(-5., 0, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-120,-160, 100)) * np.pi / 180., '-',
    #                color='r', lw=2, alpha=0.2)

    for line in np.arange(-10., 40, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-142.5,-180, 100)) * np.pi / 180., '-',
                   color='r', lw=2, alpha=0.2)

    # for line in np.arange(30., 40, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-165,-120., 100)) * np.pi / 180., '-',
    #                color='r', lw=2, alpha=0.2)

    l_start = [-12,210]
    l_end = [12,260]
    #
    # # brange = [0.5,2,5,8,10,12]
    brange = np.arange(-10, 10)
    #
    for b in brange:
        for il in range(len(l_start)):
            H.projplot(np.zeros(100.) + (90.-b) * np.pi / 180.,
                       np.linspace(l_start[il] * np.pi / 180., l_end[il] * np.pi / 180., 100),
                       'r-',lw=1,alpha=0.8,coord=['G','E'])

        # H.projplot(np.zeros(100.) + (90.-b) * np.pi / 180.,
        #            np.linspace(l_start[0] * np.pi / 180., l_end[0] * np.pi / 180., 100),
        #            'r-',lw=1,alpha=0.8,coord=['G','E'])
        #
        # H.projplot(np.zeros(100.) + (90.+b) * np.pi / 180.,
        #            np.linspace(l_start[0] * np.pi / 180., l_end[0] * np.pi / 180., 100),
        #            'r-',lw=1,alpha=0.8,coord=['G','E'])
        #
        # H.projplot(np.zeros(100.) + (90.-b) * np.pi / 180.,
        #            np.linspace(l_start[1] * np.pi / 180., l_end[1] * np.pi / 180., 100),
        #            'r-',lw=1,alpha=0.8,coord=['G','E'])
        #
        # H.projplot(np.zeros(100.) + (90.+b) * np.pi / 180.,
        #            np.linspace(l_start[1] * np.pi / 180., l_end[1] * np.pi / 180., 100),
        #            'r-',lw=1,alpha=0.8,coord=['G','E'])

    # H.projplot(np.zeros(100.) + 85. * np.pi / 180.,
    #            np.linspace(-10. * np.pi / 180., -30. * np.pi / 180., 100),
    #            'r-',lw=2,alpha=0.2,coord=['G','E'])
    #
    # H.projplot(np.zeros(100.) + 95. * np.pi / 180.,
    #            np.linspace(-10. * np.pi / 180., -30. * np.pi / 180., 100),
    #            'r-',lw=2,alpha=0.2,coord=['G','E'])
    #
    # H.projplot(np.zeros(100.) + 82. * np.pi / 180.,
    #            np.linspace(-10. * np.pi / 180., -30. * np.pi / 180., 100),
    #            'r-',lw=2,alpha=0.2,coord=['G','E'])
    #
    # H.projplot(np.zeros(100.) + 98. * np.pi / 180.,
    #            np.linspace(-10. * np.pi / 180., -30. * np.pi / 180., 100),
    #            'r-',lw=2,alpha=0.2,coord=['G','E'])
    #
    # H.projplot(np.zeros(100.) + 90. * np.pi / 180.,
    #            np.linspace(210. * np.pi / 180., 230. * np.pi / 180., 100),
    #            'r-',lw=2,alpha=0.2,coord=['G','E'])

    # H.projplot(np.zeros(100.) + 92. * np.pi / 180.,
    #            np.linspace(170. * np.pi / 180., 150. * np.pi / 180., 100),
    #            'r-',lw=2,alpha=0.2,coord=['G','E'])

    H.projplot((90 - sn_tiles[1]) * np.pi / 180., sn_tiles[0] * np.pi / 180., 's', color='r', alpha=0.8,
               coord='E')  #,coord=['E','G'])

    H.graticule()
    # py.show()
    #
    # return 0

    # END S-PLUS
    ####################################################################################################################
    # ATLAS

    for line in np.arange(10, 40, 1.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-37.5, 60, 100)) * np.pi / 180., ':',
                   color='g', lw=2, alpha=0.9)
    H.projplot((90 - np.zeros(100) + 42) * np.pi / 180., (np.linspace(-37.5, 61, 100)) * np.pi / 180., '-', color='g',
               lw=3)
    H.projplot((90 - np.zeros(100) + 10) * np.pi / 180., (np.linspace(-37.5, 61, 100)) * np.pi / 180., '-', color='g',
               lw=2)
    H.projplot((90 - np.linspace(-40, -10, 100)) * np.pi / 180., (np.zeros(100) + 62) * np.pi / 180., '-', color='g',
               lw=3)
    H.projplot((90 - np.linspace(-40, -10, 100)) * np.pi / 180., (np.zeros(100) - 37.5) * np.pi / 180., '-', color='g',
               lw=2)

    for line in np.arange(2, 29, 1.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(150, 180, 100)) * np.pi / 180., ':',
                   color='g', lw=2, alpha=0.9)
        if line < 20:
            H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-180, -127.5, 100)) * np.pi / 180., ':',
                       color='g', lw=2, alpha=0.9)
        else:
            H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-180, -135, 100)) * np.pi / 180., ':',
                       color='g', lw=2, alpha=0.9)

    H.projplot((90 - np.zeros(100) + 29) * np.pi / 180., (np.linspace(150, 180, 100)) * np.pi / 180., '-', color='g',
               lw=2)
    H.projplot((90 - np.zeros(100) + 20) * np.pi / 180., (np.linspace(-135, -127.5, 100)) * np.pi / 180., '-',
               color='g', lw=2)
    H.projplot((90 - np.zeros(100) + 29) * np.pi / 180., (np.linspace(-180, -135., 100)) * np.pi / 180., '-', color='g',
               lw=2)

    H.projplot((90 - np.zeros(100) + 2) * np.pi / 180., (np.linspace(150, 180, 100)) * np.pi / 180., '-', color='g',
               lw=2)
    H.projplot((90 - np.zeros(100) + 2) * np.pi / 180., (np.linspace(-180, -127.5, 100)) * np.pi / 180., '-', color='g',
               lw=2)

    H.projplot((90 - np.linspace(-29, -2, 100)) * np.pi / 180., (np.zeros(100) + 150) * np.pi / 180., '-', color='g',
               lw=2)
    H.projplot((90 - np.linspace(-20, -2, 100)) * np.pi / 180., (np.zeros(100) - 127.5) * np.pi / 180., '-', color='g',
               lw=2)
    H.projplot((90 - np.linspace(-29, -20, 100)) * np.pi / 180., (np.zeros(100) - 135) * np.pi / 180., '-', color='g',
               lw=2)

    # H.projplot((90 - pt_splus[1]) * np.pi / 180., pt_splus[0] * np.pi / 180., 's', color='r', alpha=0.8,
    #            coord='E')  #,coord=['E','G'])

    ra = np.linspace(-np.pi,np.pi,100.)
    dec = np.zeros(100)+(90+20*np.sin(ra))*np.pi/180.
    H.projplot(dec,ra,'-',color='w',lw=2.)
    H.projplot(dec,ra,'--',color='k',lw=2.)

    H.graticule()
    #
    # py.savefig(os.path.expanduser('~/Desktop/figure_01.pdf'))
    #
    # py.savefig(os.path.expanduser('~/Desktop/figure_01.pdf'))
    # py.show()
    #
    # return 0

    ####################################################################################################################
    # Vista
    #
    ## VVV Bulge
    #

    b = np.append(np.append(np.append(np.linspace(80. * np.pi / 180., 95. * np.pi / 180., 100),
                                      np.zeros(100.) + 80. * np.pi / 180.),
                            np.linspace(80. * np.pi / 180., 95. * np.pi / 180., 100)),
                  np.zeros(100) + 96. * np.pi / 180.)

    l = np.append(np.append(np.append(np.zeros(100.) + 10. * np.pi / 180.,
                                      np.linspace(-10. * np.pi / 180., 10. * np.pi / 180., 100)),
                            np.zeros(100) - 10. * np.pi / 180.),
                  np.linspace(-10. * np.pi / 180., 10. * np.pi / 180., 100))
    H.projplot(b,l,'-',color="0.5",lw=2,coord=['G','E'])

    #
    ## VVV Disk
    #

    b = np.append(np.append(np.append(np.linspace(88. * np.pi / 180., 92. * np.pi / 180., 100),
                                      np.zeros(100.) + 88. * np.pi / 180.),
                            np.linspace(88. * np.pi / 180., 92. * np.pi / 180., 100)),
                  np.zeros(100) + 92. * np.pi / 180.)

    l = np.append(np.append(np.append(np.zeros(100.) - 10. * np.pi / 180.,
                                      np.linspace(-10. * np.pi / 180., -65. * np.pi / 180., 100)),
                            np.zeros(100) - 65. * np.pi / 180.),
                  np.linspace(-65. * np.pi / 180., -10. * np.pi / 180., 100))
    H.projplot(b,l,'-',color="0.5",lw=2,coord=['G','E'])


    ##################################
    # VPHAS

    vb = np.append(np.append(np.append(np.linspace(80. * np.pi / 180., 100. * np.pi / 180., 100),
                                      np.zeros(100.) + 80. * np.pi / 180.),
                            np.linspace(80. * np.pi / 180., 100. * np.pi / 180., 100)),
                  np.zeros(100) + 100. * np.pi / 180.)

    vl = np.append(np.append(np.append(np.zeros(100.) + 10. * np.pi / 180.,
                                      np.linspace(-10. * np.pi / 180., 10. * np.pi / 180., 100)),
                            np.zeros(100) - 10. * np.pi / 180.),
                  np.linspace(-10. * np.pi / 180., 10. * np.pi / 180., 100))
    # H.projplot(vb,vl,'r-',lw=2,coord=['G','E'])

    #
    ## VPHAS Disk
    #

    vb = np.append(np.append(np.append(np.linspace(85. * np.pi / 180., 95. * np.pi / 180., 100),
                                      np.zeros(100.) + 85. * np.pi / 180.),
                            np.linspace(85. * np.pi / 180., 95. * np.pi / 180., 100)),
                  np.zeros(100) + 95. * np.pi / 180.)

    vl = np.append(np.append(np.append(np.zeros(100.) + 40. * np.pi / 180.,
                                      np.linspace(40. * np.pi / 180., -160. * np.pi / 180., 100)),
                            np.zeros(100) - 160. * np.pi / 180.),
                  np.linspace(-160. * np.pi / 180., 40. * np.pi / 180., 100))
    H.projplot(vb,vl,'m-',lw=2,coord=['G','E'])

    ##################################
    # Avoiding region
    vb = np.zeros(100.) + 120. * np.pi / 180.
    vl = np.linspace(0. * np.pi / 180., 360. * np.pi / 180., 100)
    H.projplot(vb,vl,'w--',lw=2,coord=['G','E'])

    #
    ## DECAL
    #
    for line in np.arange(-30, 10, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(120, 240, 100)) * np.pi / 180., ':',
                   color='k', lw=2, alpha=0.9)

    for line in np.arange(-30, -15, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-30, 40, 100)) * np.pi / 180., ':',
                   color='k', lw=2, alpha=0.9)

    for line in np.arange(-15, -1, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-45, 40, 100)) * np.pi / 180., ':',
                   color='k', lw=2, alpha=0.9)

    for line in np.arange(-10, 10, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(40, 60, 100)) * np.pi / 180., ':',
                   color='k', lw=2, alpha=0.9)

    for line in np.arange(1, 10, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-0, -45, 100)) * np.pi / 180., ':',
                   color='k', lw=2, alpha=0.9)

    ##

    a = [0,0,5,5]
    d = [-3,+3,+3,-3]
    for d in np.arange(-3,3,0.5):
        H.projplot((90 - np.zeros(100) + d) * np.pi / 180., (np.linspace(0, 5, 100)) * np.pi / 180., '-', color='c',
               lw=2)

    # H.projplot((90 + np.linspace(10, 30, 100)) * np.pi / 180., (np.zeros(100) + 61) * np.pi / 180., '-', color='r',
    #            lw=2)
    # H.projplot((90 - np.zeros(100) + 30) * np.pi / 180., (np.linspace(60, 90, 100)) * np.pi / 180., '-', color='r',
    #            lw=2)
    # H.projplot((90 + np.linspace(30, 80, 100)) * np.pi / 180., (np.zeros(100) + 90) * np.pi / 180., '-', color='r',
    #            lw=2)
    # H.projplot((90 - np.zeros(100) + 80) * np.pi / 180., (np.linspace(-90, 90, 100)) * np.pi / 180., '-', color='r',
    #            lw=2)
    # H.projplot((90 + np.linspace(45, 80, 100)) * np.pi / 180., (np.zeros(100) - 90) * np.pi / 180., '-', color='r',
    #            lw=2)
    # H.projplot((90 - np.zeros(100) + 45) * np.pi / 180., (np.linspace(-90, -60, 100)) * np.pi / 180., '-', color='r',
    #            lw=2)
    # H.projplot((90 + np.linspace(10, 45, 100)) * np.pi / 180., (np.zeros(100) -60) * np.pi / 180., '-', color='r',
    #            lw=2)

    #
    # H.projplot((90 - nna_pt[1]) * np.pi / 180., nna_pt[0] * np.pi / 180., '.', color='r', alpha=0.2,
    #            coord='E')  #,coord=['E','G'])
    # H.projplot((90 - nsa_pt[1]) * np.pi / 180., nsa_pt[0] * np.pi / 180., '.', color='r', alpha=0.2,
    #            coord='E')  #,coord=['E','G'])
    #
    # H.projplot( (90-pt_kepler[1]) * np.pi/180. , pt_kepler[0] * np.pi /180., '-', color='c', alpha=1.0,
    #            coord='E',lw=2)  #,coord=['E','G'])


    # H.projplot((90 - pt_smaps_sul[1]) * np.pi / 180., pt_smaps_sul[0] * np.pi / 180., '.', color='r', alpha=0.2,
    #            coord='E')  #,coord=['E','G'])
    # H.projplot((90 - pt_smaps_nor[1]) * np.pi / 180., pt_smaps_nor[0] * np.pi / 180., '.', color='r', alpha=0.8,
    #            coord='E')  #,coord=['E','G'])

    # H.projplot((90 - pt_spp[1]) * np.pi / 180., pt_spp[0] * np.pi / 180., 'o',
    #            color='b', coord='E')  #,coord=['E','G'])

    #H.projplot((90-pt_smaps_lmc[1])*np.pi/180.,pt_smaps_lmc[0]*np.pi/180.,'.',color='k',alpha=1,coord='E')#,coord=['E','G'])
    #H.projplot((90-pt_smaps_smc[1])*np.pi/180.,pt_smaps_smc[0]*np.pi/180.,'.',color='k',alpha=1,coord='E')#,coord=['E','G'])

    H.graticule()

    # py.show()
    #
    # return 0

    # SPT

    H.projplot((90 - np.zeros(100) + 65) * np.pi / 180., (np.linspace(-60, 105, 100)) * np.pi / 180., '-', color='b',
               lw=2)

    # for line in np.arange(40, 65, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-60, 105, 100)) * np.pi / 180., '-',
    #                color='b', lw=2, alpha=0.5)
    H.projplot((90 - np.zeros(100) + 40) * np.pi / 180., (np.linspace(-60, 105, 100)) * np.pi / 180., '-', color='b',
               lw=2)
    # H.projplot((90 - np.zeros(100) + 40) * np.pi / 180., (np.linspace(-30, 105, 100)) * np.pi / 180., '--', color='b',
    #            lw=2)
    # H.projplot((90 - np.zeros(100) + 40) * np.pi / 180., (np.linspace(+60, 105, 100)) * np.pi / 180., '-', color='b',
    #            lw=2)

    H.projplot((90 - np.linspace(-65, -40, 100)) * np.pi / 180., (np.zeros(100) - 60) * np.pi / 180., '-', color='b',
               lw=2)
    H.projplot((90 - np.linspace(-65, -40, 100)) * np.pi / 180., (np.zeros(100) + 105) * np.pi / 180., '-', color='b',
               lw=2)

    # VIKING
    # for line in np.arange(25, 40, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-30, 60, 100)) * np.pi / 180., '-',
    #                color='b', lw=2, alpha=0.5)
    H.projplot((90 - np.linspace(-40, -25, 100)) * np.pi / 180., (np.zeros(100) - 30) * np.pi / 180., '-', color='b',
               lw=2)
    H.projplot((90 - np.linspace(-40, -25, 100)) * np.pi / 180., (np.zeros(100) + 60) * np.pi / 180., '-', color='b',
               lw=2)
    H.projplot((90 - np.zeros(100) + 25) * np.pi / 180., (np.linspace(-30, 60, 100)) * np.pi / 180., '-', color='b',
               lw=2)

    # ROUND 82
    # for line in np.arange(-3, 45, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-25, 3, 100)) * np.pi / 180., '-',
    #                color='b', lw=2, alpha=0.5)
    # H.projplot((90 - np.linspace(3, -45, 100)) * np.pi / 180., (np.zeros(100) - 25) * np.pi / 180., '-', color='b',
    #            lw=2)
    # H.projplot((90 - np.linspace(3, -45, 100)) * np.pi / 180., (np.zeros(100) + 3) * np.pi / 180., '-', color='b', lw=2)
    # H.projplot((90 - np.zeros(100) + 45) * np.pi / 180., (np.linspace(-25, 3, 100)) * np.pi / 180., '-', color='b',
    #            lw=2)
    # H.projplot((90 - np.zeros(100) - 3) * np.pi / 180., (np.linspace(-25, 3, 100)) * np.pi / 180., '-', color='b', lw=2)

    H.projplot((90 - np.linspace(3, -25, 100)) * np.pi / 180., (np.zeros(100) + 45) * np.pi / 180., '-', color='b',
               lw=2)
    H.projplot((90 - np.linspace(3, -25, 100)) * np.pi / 180., (np.zeros(100) - 3) * np.pi / 180., '-', color='b', lw=2)
    H.projplot((90 - np.zeros(100) + 25) * np.pi / 180., (np.linspace(+45, -3, 100)) * np.pi / 180., '-', color='b',
               lw=2)
    H.projplot((90 - np.zeros(100) - 3) * np.pi / 180., (np.linspace(+45, -3, 100)) * np.pi / 180., '-', color='b', lw=2)

    # STRIPE 82
    H.projplot((90 - np.linspace(-1, +1, 100)) * np.pi / 180., (np.zeros(100) + 3) * np.pi / 180., '-', color='b', lw=2)
    H.projplot((90 - np.linspace(-1, +1, 100)) * np.pi / 180., (np.zeros(100) + 43) * np.pi / 180., '-', color='b',
               lw=2)
    H.projplot((90 - np.zeros(100) + 1) * np.pi / 180., (np.linspace(-3, -43, 100)) * np.pi / 180., '-', color='b',
               lw=2)
    H.projplot((90 - np.zeros(100) - 1) * np.pi / 180., (np.linspace(-3, -43, 100)) * np.pi / 180., '-', color='b',
               lw=2)

    # KIDS

    H.projplot((90 - np.linspace(-5, +5, 100)) * np.pi / 180., (np.zeros(100) - 120) * np.pi / 180., '-', color='y',
               lw=2)
    H.projplot((90 - np.linspace(-5, +5, 100)) * np.pi / 180., (np.zeros(100) - 202.5) * np.pi / 180., '-', color='y',
               lw=2)

    for line in np.arange(-5, 5, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-120, -180, 100)) * np.pi / 180., '-',
                   color='y', lw=2, alpha=0.5)
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(157, 180, 100)) * np.pi / 180., '-',
                   color='y', lw=2, alpha=0.5)
    H.projplot((90 - np.zeros(100) - 5) * np.pi / 180., (np.linspace(157, 180, 100)) * np.pi / 180., '-', color='y',
               lw=2)
    H.projplot((90 - np.zeros(100) + 5) * np.pi / 180., (np.linspace(157, 180, 100)) * np.pi / 180., '-', color='y',
               lw=2)

    H.projplot((90 - np.zeros(100) - 5) * np.pi / 180., (np.linspace(-120, -180, 100)) * np.pi / 180., '-', color='y',
               lw=2)
    H.projplot((90 - np.zeros(100) + 5) * np.pi / 180., (np.linspace(-120, -180, 100)) * np.pi / 180., '-', color='y',
               lw=2)

    H.projplot((90 - np.linspace(-30, -25, 100)) * np.pi / 180., (np.zeros(100) - 30) * np.pi / 180., '-', color='y',
               lw=2)
    H.projplot((90 - np.linspace(-30, -25, 100)) * np.pi / 180., (np.zeros(100) + 53.5) * np.pi / 180., '-', color='y',
               lw=2)

    for line in np.arange(-30, -25, 0.5):
        H.projplot((90 - np.zeros(100) - line) * np.pi / 180., (np.linspace(-30.5, 53.5, 100)) * np.pi / 180., '-',
                   color='y', lw=2, alpha=0.5)

    H.projplot((90 - np.zeros(100) + 30) * np.pi / 180., (np.linspace(-30, 30, 100)) * np.pi / 180., '-', color='y',
               lw=2)
    H.projplot((90 - np.zeros(100) + 25) * np.pi / 180., (np.linspace(-30, 30, 100)) * np.pi / 180., '-', color='y',
               lw=2)

    #
    ## GAMMA
    #
    # G02  30.2 :  38.8 / -10.25 :  -3.72
    # G09 129.0 : 141.0 /  -2    :  +3
    # G12 174.0 : 186.0 /  -3    :  +2
    # G15 211.5 : 223.5 /  -2    :  +3
    # G23 339.0 : 351.0 / -35    : -30

    for line in np.arange(3.72, 10.25, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(30.2, 38.8, 100)) * np.pi / 180., '-',
                   color='#66FF33', lw=2, alpha=0.9)
    for line in np.arange(-3, 2, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(129., 141., 100)) * np.pi / 180., '-',
                   color='#66FF33', lw=2, alpha=0.9)
    for line in np.arange(-2, 3, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(174, 186, 100)) * np.pi / 180., '-',
                   color='#66FF33', lw=2, alpha=0.9)
    for line in np.arange(-3, -2, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(211.5, 223.5, 100)) * np.pi / 180., '-',
                   color='#66FF33', lw=2, alpha=0.9)
    for line in np.arange(30, 35, 0.5):
        H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(339, 351, 100)) * np.pi / 180., '-',
                   color='#66FF33', lw=2, alpha=0.9)

    #
    ## VIKING
    #

    #SGP:        22h00 < RA < 03h30 ,     -36 < Dec < -26 deg.
    # H.projplot((90 - np.zeros(100) + 45.) * np.pi / 180., (np.linspace(-36, -26, 100)) * np.pi / 180., '-', color='k',
    #            lw=2)
    # H.projplot((90 - np.linspace(-45, 30, 100)) * np.pi / 180., (np.zeros(100) - 36) * np.pi / 180., '-', color='k',
    #            lw=2)
    # H.projplot((90 - np.zeros(100) - 30.) * np.pi / 180., (np.linspace(-36, -26, 100)) * np.pi / 180., '-', color='k',
    #            lw=2)
    # H.projplot((90 - np.linspace(-45, 30, 100)) * np.pi / 180., (np.zeros(100) - 26) * np.pi / 180., '-', color='k',
    #            lw=2)
    # # for line in np.arange(-45, 30, 0.5):
    # #     H.projplot((90 - np.zeros(100) - line) * np.pi / 180., (np.linspace(-36, -26, 100)) * np.pi / 180., '-',
    # #                color='k', lw=2, alpha=0.5)
    # #NGP:        10h00 < RA < 15h30,      -5 < Dec < +4 deg
    # H.projplot((90 - np.zeros(100) + 150.) * np.pi / 180., (np.linspace(-5, 4, 100)) * np.pi / 180., '-', color='k',
    #            lw=2)
    # H.projplot((90 - np.linspace(-150, -232.5, 100)) * np.pi / 180., (np.zeros(100) + 4) * np.pi / 180., '-', color='k',
    #            lw=2)
    # H.projplot((90 - np.zeros(100) + 232.5) * np.pi / 180., (np.linspace(-5, +4, 100)) * np.pi / 180., '-', color='k',
    #            lw=2)
    # H.projplot((90 - np.linspace(-150, -232.5, 100)) * np.pi / 180., (np.zeros(100) - 5) * np.pi / 180., '-', color='k',
    #            lw=2)
    # for line in np.arange(150, 232.5, 0.5):
    #     H.projplot((90 - np.zeros(100) + line) * np.pi / 180., (np.linspace(-5, +4, 100)) * np.pi / 180., '-',
    #                color='k', lw=2, alpha=0.5)

    ####################################################################################################################
    # Ecliptic
    #

    # ra = np.linspace(-np.pi,np.pi,100.)
    # dec = np.zeros(100)+(90+20*np.sin(ra))*np.pi/180.
    # H.projplot(dec,ra,'-',color='w',lw=2.)
    # H.projplot(dec,ra,'--',color='k',lw=2.)

    H.graticule()

    py.savefig(os.path.expanduser('~/Desktop/figure_01.pdf'))

    py.show()

################################################################################

if __name__ == '__main__':
    main()