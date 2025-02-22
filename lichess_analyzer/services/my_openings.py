from lichess_analyzer.services.opening_variation import OpeningVariation

# white openings
white_book_openings = OpeningVariation(None, 'e4', [
  OpeningVariation('e5', 'Nf3', [
    OpeningVariation('Nc6', 'Bc4', [
      OpeningVariation('Nf6', 'Ng5', comment='Start of Fried Liver', followed_by=[
        OpeningVariation('Bc5', 'Bf7', [
          OpeningVariation('Kf8', 'Bb3'),
          OpeningVariation('Ke7', 'Bf5', comment='castle afterwards and look for Bg5')
        ]),
        OpeningVariation('d5', 'exd5', [
          OpeningVariation('Nxd5', 'Nxf7', [
            OpeningVariation('Kxf7', 'Qf3', [
              OpeningVariation('Qf6', 'Bxd5', [
                OpeningVariation('Be6', 'Bxc6', [
                  OpeningVariation('xc6', 'Qxc6', [
                    OpeningVariation('Bd6', 'Nc3',[
                      OpeningVariation('Rhf8', 'd3', [
                        OpeningVariation('Kg8', 'O-O')
                      ])
                    ])
                  ])
                ])
              ]),
              OpeningVariation('Kg8', 'Bd5', [
                OpeningVariation('Qxd5', 'Qxd5', comment='mate')
              ]),
              OpeningVariation('Ke8', 'Bd5'),
              OpeningVariation('Ke6', 'Nc3', [
                OpeningVariation('Nd4', 'Bd5', [
                  OpeningVariation('Kc5', 'Qf7', [
                    OpeningVariation('Kd6', 'Ne4', comment='mate')
                  ])
                ]),
                OpeningVariation('Nb4', 'O-O', [
                  OpeningVariation('c6', 'd4', [
                    OpeningVariation('Qf6', 'Qe2', [
                      OpeningVariation('Bd6', 'f4', [
                        OpeningVariation('e4', 'Ne4')
                      ]),
                      OpeningVariation('Ke7', 'Ne4', [
                        OpeningVariation('c3', 'Bf5', [
                        ])
                      ])
                    ])
                  ]),
                  OpeningVariation('Nc2', 'Bd5'),
                  OpeningVariation('c6', 'd4', [
                    OpeningVariation('Nxc2', 'dxe5', [
                      OpeningVariation('Nxa1', 'Nxd5', [
                        OpeningVariation('cxd5', 'Rf1', [
                          OpeningVariation('Qa5', 'Bxd5', [
                            OpeningVariation('Ke7', 'Qf7', [
                              OpeningVariation('Kd8', 'Bg5')
                            ])
                          ])
                        ])
                      ])
                    ])
                  ]),
                ])
              ]),
              OpeningVariation('Qf6', 'Bxd5', [
                OpeningVariation('Be6', 'Bxc6', [
                  OpeningVariation('bxc6', 'Qxc6', [
                    OpeningVariation('Bd6', 'Nc3', [
                      OpeningVariation('Rhf8', 'd3', [
                        OpeningVariation('Kg8', 'O-O')
                      ])
                    ])
                  ])
                ])
              ])
            ])
          ]),
          OpeningVariation('Na5', 'Bb5', [
            OpeningVariation('c6', 'dxc6', [
              OpeningVariation('bxc6', 'Bd3', [
                OpeningVariation('h6', 'Ne4', [
                  OpeningVariation('Nxe4', 'Bxe4', [
                    OpeningVariation('Bc5', 'O-O')
                  ])
                ]),
                OpeningVariation('Nxd5', 'Nf3', [
                  OpeningVariation('Bd6', 'O-O', [
                    OpeningVariation('O-O', 'Re1', [
                      OpeningVariation('Re8', 'Nc3',[
                        OpeningVariation('f5', 'Nxd5', [
                          OpeningVariation('cxd5', 'Bf1')
                        ])
                      ]),
                      OpeningVariation('f5', 'Re5', [
                        OpeningVariation('Bxe5', 'Nxe5')
                      ])
                    ]),
                  ])
                ])
              ])
            ]),
            OpeningVariation('Bd7', 'Qe2', [
              OpeningVariation('Bd6', 'Bxd7', [
                OpeningVariation('Qxd7', 'Nc3')
              ])
            ])
          ]),
          OpeningVariation('Nd4', 'c3', [
            OpeningVariation('b5', 'Bf1', [
              OpeningVariation('Nxd5', 'cxd4', [
                OpeningVariation('Qxg5', 'Bb5', [
                  OpeningVariation('Kd8', 'O-O', [
                    OpeningVariation('Bb7', 'Qf3', [
                      OpeningVariation('Rb8', 'dxe5', [
                        OpeningVariation('Ne3', 'Qh3')
                      ])
                    ])
                  ])
                ])
              ])
            ])
          ]),
          OpeningVariation('b5', 'Bf1',[
            OpeningVariation('Nxd5','Bxb5', [
              OpeningVariation('Bd7', 'd3', [
                OpeningVariation('Be7', 'Nxf7',[
                  OpeningVariation('Kxf7', 'Qf3',[
                    OpeningVariation('Ke6', 'Nc3',[
                      OpeningVariation('Nxc3', 'Bc4',[
                        OpeningVariation('Kd6', 'bxc3')
                      ])
                    ])
                  ])
                ])
              ]),
              OpeningVariation('Bb7', 'd3')
            ]),
            OpeningVariation('Qxd5', 'Nc3', [
              OpeningVariation('Qc5', 'Bxb5')
            ])
          ])
        ])
      ])
    ])
  ])
])