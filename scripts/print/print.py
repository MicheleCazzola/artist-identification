string1 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model.pth', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 184MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 30, Loss: 5.46236
INFO:root:Training epoch 1, Iteration 60, Loss: 4.99470
INFO:root:Training epoch 1, Iteration 90, Loss: 4.93048
INFO:root:Training epoch 1, Iteration 120, Loss: 4.96051
INFO:root:Training epoch 1, Iteration 150, Loss: 4.75235
INFO:root:Training epoch 1, Iteration 180, Loss: 4.84778
INFO:root:Training epoch 1, Iteration 210, Loss: 4.81725
INFO:root:Training epoch 1, Iteration 240, Loss: 4.85274
INFO:root:Training epoch 1, Iteration 270, Loss: 4.82491
INFO:root:Training epoch 1, Iteration 300, Loss: 4.82534
INFO:root:Training epoch 1, Iteration 330, Loss: 4.68327
INFO:root:Training epoch 1, Iteration 360, Loss: 4.68235
INFO:root:Training epoch 1, Iteration 390, Loss: 4.70917
INFO:root:Training epoch 1, Iteration 420, Loss: 4.65332
INFO:root:Training epoch 1, Iteration 450, Loss: 4.65226
INFO:root:Training epoch 1, Iteration 480, Loss: 4.67778
INFO:root:Training epoch 1, Iteration 510, Loss: 4.80637
INFO:root:Training epoch 1, Iteration 540, Loss: 4.61622
INFO:root:Training epoch 1, Iteration 570, Loss: 4.70664
INFO:root:Training epoch 1, Iteration 600, Loss: 4.68429
INFO:root:Training epoch 1, Iteration 630, Loss: 4.68612
INFO:root:Training epoch 1, Iteration 660, Loss: 4.58470
INFO:root:Training epoch 1, Iteration 690, Loss: 4.56855
INFO:root:Training epoch 1, Iteration 720, Loss: 4.63013
INFO:root:Training epoch 1, Iteration 750, Loss: 4.61481
INFO:root:Training epoch 1, Iteration 780, Loss: 4.48662
INFO:root:Validation iteration 10, Loss: 4.46507
INFO:root:Validation iteration 20, Loss: 4.48436
INFO:root:Validation iteration 30, Loss: 4.51416
INFO:root:Validation iteration 40, Loss: 4.45316
INFO:root:Validation iteration 50, Loss: 4.53775
INFO:root:Validation iteration 60, Loss: 4.42903
INFO:root:Validation iteration 70, Loss: 4.66250
INFO:root:Validation iteration 80, Loss: 4.52121
INFO:root:Validation iteration 90, Loss: 4.63304
INFO:root:Validation iteration 100, Loss: 4.51363
INFO:root:Validation iteration 110, Loss: 4.52783
INFO:root:Validation iteration 120, Loss: 4.42808
INFO:root:Validation iteration 130, Loss: 4.54432
INFO:root:Validation iteration 140, Loss: 4.63058
INFO:root:Validation iteration 150, Loss: 4.76443
INFO:root:Validation iteration 160, Loss: 4.54328
INFO:root:Validation iteration 170, Loss: 4.54342
INFO:root:Validation iteration 180, Loss: 4.61335
INFO:root:Validation iteration 190, Loss: 4.44050
INFO:root:Validation iteration 200, Loss: 4.53330
INFO:root:Validation iteration 210, Loss: 4.70270
INFO:root:Validation iteration 220, Loss: 4.57359
INFO:root:Validation iteration 230, Loss: 4.70695
INFO:root:Validation iteration 240, Loss: 4.64484
INFO:root:Validation iteration 250, Loss: 4.55682
INFO:root:Validation iteration 260, Loss: 4.59309
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.755
INFO:root:Validation accuracy: 0.015, Validation loss: 4.56025
INFO:root:Training epoch 2, Iteration 30, Loss: 4.59523
INFO:root:Training epoch 2, Iteration 60, Loss: 4.58383
INFO:root:Training epoch 2, Iteration 90, Loss: 4.60609
INFO:root:Training epoch 2, Iteration 120, Loss: 4.54776
INFO:root:Training epoch 2, Iteration 150, Loss: 4.42405
INFO:root:Training epoch 2, Iteration 180, Loss: 4.44808
INFO:root:Training epoch 2, Iteration 210, Loss: 4.57538
INFO:root:Training epoch 2, Iteration 240, Loss: 4.51447
INFO:root:Training epoch 2, Iteration 270, Loss: 4.51446
INFO:root:Training epoch 2, Iteration 300, Loss: 4.59305
INFO:root:Training epoch 2, Iteration 330, Loss: 4.60591
INFO:root:Training epoch 2, Iteration 360, Loss: 4.52964
INFO:root:Training epoch 2, Iteration 390, Loss: 4.60197
INFO:root:Training epoch 2, Iteration 420, Loss: 4.65223
INFO:root:Training epoch 2, Iteration 450, Loss: 4.63119
INFO:root:Training epoch 2, Iteration 480, Loss: 4.54748
INFO:root:Training epoch 2, Iteration 510, Loss: 4.47765
INFO:root:Training epoch 2, Iteration 540, Loss: 4.56696
INFO:root:Training epoch 2, Iteration 570, Loss: 4.57295
INFO:root:Training epoch 2, Iteration 600, Loss: 4.53342
INFO:root:Training epoch 2, Iteration 630, Loss: 4.56723
INFO:root:Training epoch 2, Iteration 660, Loss: 4.54494
INFO:root:Training epoch 2, Iteration 690, Loss: 4.62445
INFO:root:Training epoch 2, Iteration 720, Loss: 4.56235
INFO:root:Training epoch 2, Iteration 750, Loss: 4.47740
INFO:root:Training epoch 2, Iteration 780, Loss: 4.49503
INFO:root:Validation iteration 10, Loss: 4.47707
INFO:root:Validation iteration 20, Loss: 4.46358
INFO:root:Validation iteration 30, Loss: 4.45156
INFO:root:Validation iteration 40, Loss: 4.41049
INFO:root:Validation iteration 50, Loss: 4.57556
INFO:root:Validation iteration 60, Loss: 4.29416
INFO:root:Validation iteration 70, Loss: 4.57636
INFO:root:Validation iteration 80, Loss: 4.47163
INFO:root:Validation iteration 90, Loss: 4.62781
INFO:root:Validation iteration 100, Loss: 4.52619
INFO:root:Validation iteration 110, Loss: 4.47756
INFO:root:Validation iteration 120, Loss: 4.38136
INFO:root:Validation iteration 130, Loss: 4.50893
INFO:root:Validation iteration 140, Loss: 4.61629
INFO:root:Validation iteration 150, Loss: 4.70287
INFO:root:Validation iteration 160, Loss: 4.52708
INFO:root:Validation iteration 170, Loss: 4.56859
INFO:root:Validation iteration 180, Loss: 4.63429
INFO:root:Validation iteration 190, Loss: 4.41818
INFO:root:Validation iteration 200, Loss: 4.48989
INFO:root:Validation iteration 210, Loss: 4.68161
INFO:root:Validation iteration 220, Loss: 4.60941
INFO:root:Validation iteration 230, Loss: 4.74498
INFO:root:Validation iteration 240, Loss: 4.63752
INFO:root:Validation iteration 250, Loss: 4.50668
INFO:root:Validation iteration 260, Loss: 4.56510
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.553
INFO:root:Validation accuracy: 0.015, Validation loss: 4.53546
INFO:root:Best validation accuracy: 0.015 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 10, Loss: 4.40843
INFO:root:Validation iteration 20, Loss: 4.49850
INFO:root:Validation iteration 30, Loss: 4.50850
INFO:root:Validation iteration 40, Loss: 4.56525
INFO:root:Validation iteration 50, Loss: 4.66124
INFO:root:Validation iteration 60, Loss: 4.49606
INFO:root:Validation iteration 70, Loss: 4.55209
INFO:root:Validation iteration 80, Loss: 4.74412
INFO:root:Validation iteration 90, Loss: 4.45226
INFO:root:Validation iteration 100, Loss: 4.61516
INFO:root:Validation iteration 110, Loss: 4.52264
INFO:root:Validation iteration 120, Loss: 4.54825
INFO:root:Validation iteration 130, Loss: 4.53246
INFO:root:Validation iteration 140, Loss: 4.58172
INFO:root:Validation iteration 150, Loss: 4.60642
INFO:root:Validation iteration 160, Loss: 4.44028
INFO:root:Validation iteration 170, Loss: 4.50363
INFO:root:Validation iteration 180, Loss: 4.45696
INFO:root:Validation iteration 190, Loss: 4.42116
INFO:root:Validation iteration 200, Loss: 4.56078
INFO:root:Validation iteration 210, Loss: 4.49132
INFO:root:Validation iteration 220, Loss: 4.51009
INFO:root:Validation iteration 230, Loss: 35.77434
INFO:root:Validation iteration 240, Loss: 4.60491
INFO:root:Validation iteration 250, Loss: 4.35147
INFO:root:Validation iteration 260, Loss: 4.61815
Test accuracy: 0.016, Test loss: 5.70806
INFO:root:Saving results...
INFO:root:Done!
"""

string2 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model.pth', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=True, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 180MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 30, Loss: 5.43071
INFO:root:Training epoch 1, Iteration 60, Loss: 5.00726
INFO:root:Training epoch 1, Iteration 90, Loss: 4.86429
INFO:root:Training epoch 1, Iteration 120, Loss: 4.97362
INFO:root:Training epoch 1, Iteration 150, Loss: 4.79212
INFO:root:Training epoch 1, Iteration 180, Loss: 4.84936
INFO:root:Training epoch 1, Iteration 210, Loss: 4.74608
INFO:root:Training epoch 1, Iteration 240, Loss: 4.82762
INFO:root:Training epoch 1, Iteration 270, Loss: 4.78185
INFO:root:Training epoch 1, Iteration 300, Loss: 4.65074
INFO:root:Training epoch 1, Iteration 330, Loss: 4.78808
INFO:root:Training epoch 1, Iteration 360, Loss: 4.67464
INFO:root:Training epoch 1, Iteration 390, Loss: 4.69290
INFO:root:Training epoch 1, Iteration 420, Loss: 4.69141
INFO:root:Training epoch 1, Iteration 450, Loss: 4.65684
INFO:root:Training epoch 1, Iteration 480, Loss: 4.76726
INFO:root:Training epoch 1, Iteration 510, Loss: 4.60506
INFO:root:Training epoch 1, Iteration 540, Loss: 4.67166
INFO:root:Training epoch 1, Iteration 570, Loss: 4.65559
INFO:root:Training epoch 1, Iteration 600, Loss: 4.75935
INFO:root:Training epoch 1, Iteration 630, Loss: 4.62993
INFO:root:Training epoch 1, Iteration 660, Loss: 4.54106
INFO:root:Training epoch 1, Iteration 690, Loss: 4.58868
INFO:root:Training epoch 1, Iteration 720, Loss: 4.64647
INFO:root:Training epoch 1, Iteration 750, Loss: 4.53148
INFO:root:Training epoch 1, Iteration 780, Loss: 4.56930
INFO:root:Validation iteration 10, Loss: 5.68468
INFO:root:Validation iteration 20, Loss: 5.74822
INFO:root:Validation iteration 30, Loss: 5.62638
INFO:root:Validation iteration 40, Loss: 5.53698
INFO:root:Validation iteration 50, Loss: 5.99310
INFO:root:Validation iteration 60, Loss: 5.36391
INFO:root:Validation iteration 70, Loss: 5.82189
INFO:root:Validation iteration 80, Loss: 5.52925
INFO:root:Validation iteration 90, Loss: 5.79149
INFO:root:Validation iteration 100, Loss: 5.77626
INFO:root:Validation iteration 110, Loss: 5.52864
INFO:root:Validation iteration 120, Loss: 5.70053
INFO:root:Validation iteration 130, Loss: 5.95126
INFO:root:Validation iteration 140, Loss: 5.83821
INFO:root:Validation iteration 150, Loss: 5.93890
INFO:root:Validation iteration 160, Loss: 5.74406
INFO:root:Validation iteration 170, Loss: 5.79374
INFO:root:Validation iteration 180, Loss: 5.69663
INFO:root:Validation iteration 190, Loss: 5.62763
INFO:root:Validation iteration 200, Loss: 5.67424
INFO:root:Validation iteration 210, Loss: 5.91869
INFO:root:Validation iteration 220, Loss: 5.77238
INFO:root:Validation iteration 230, Loss: 5.95530
INFO:root:Validation iteration 240, Loss: 5.86134
INFO:root:Validation iteration 250, Loss: 5.74428
INFO:root:Validation iteration 260, Loss: 5.67941
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.745
INFO:root:Validation accuracy: 0.006, Validation loss: 5.74285
INFO:root:Training epoch 2, Iteration 30, Loss: 4.53490
INFO:root:Training epoch 2, Iteration 60, Loss: 4.62982
INFO:root:Training epoch 2, Iteration 90, Loss: 4.46753
INFO:root:Training epoch 2, Iteration 120, Loss: 4.64495
INFO:root:Training epoch 2, Iteration 150, Loss: 4.60122
INFO:root:Training epoch 2, Iteration 180, Loss: 4.47395
INFO:root:Training epoch 2, Iteration 210, Loss: 4.43454
INFO:root:Training epoch 2, Iteration 240, Loss: 4.57766
INFO:root:Training epoch 2, Iteration 270, Loss: 4.45881
INFO:root:Training epoch 2, Iteration 300, Loss: 4.50144
INFO:root:Training epoch 2, Iteration 330, Loss: 4.48740
INFO:root:Training epoch 2, Iteration 360, Loss: 4.44699
INFO:root:Training epoch 2, Iteration 390, Loss: 4.45740
INFO:root:Training epoch 2, Iteration 420, Loss: 4.42613
INFO:root:Training epoch 2, Iteration 450, Loss: 4.51303
INFO:root:Training epoch 2, Iteration 480, Loss: 4.42308
INFO:root:Training epoch 2, Iteration 510, Loss: 4.49716
INFO:root:Training epoch 2, Iteration 540, Loss: 4.51827
INFO:root:Training epoch 2, Iteration 570, Loss: 4.39847
INFO:root:Training epoch 2, Iteration 600, Loss: 4.43468
INFO:root:Training epoch 2, Iteration 630, Loss: 4.45589
INFO:root:Training epoch 2, Iteration 660, Loss: 4.40887
INFO:root:Training epoch 2, Iteration 690, Loss: 4.31482
INFO:root:Training epoch 2, Iteration 720, Loss: 4.33784
INFO:root:Training epoch 2, Iteration 750, Loss: 4.39218
INFO:root:Training epoch 2, Iteration 780, Loss: 4.41646
INFO:root:Validation iteration 10, Loss: 5.11865
INFO:root:Validation iteration 20, Loss: 5.08896
INFO:root:Validation iteration 30, Loss: 4.98512
INFO:root:Validation iteration 40, Loss: 5.20674
INFO:root:Validation iteration 50, Loss: 5.11538
INFO:root:Validation iteration 60, Loss: 5.14638
INFO:root:Validation iteration 70, Loss: 5.24493
INFO:root:Validation iteration 80, Loss: 5.31653
INFO:root:Validation iteration 90, Loss: 5.14777
INFO:root:Validation iteration 100, Loss: 5.12276
INFO:root:Validation iteration 110, Loss: 5.13951
INFO:root:Validation iteration 120, Loss: 5.11663
INFO:root:Validation iteration 130, Loss: 5.21624
INFO:root:Validation iteration 140, Loss: 5.22224
INFO:root:Validation iteration 150, Loss: 5.36666
INFO:root:Validation iteration 160, Loss: 5.13700
INFO:root:Validation iteration 170, Loss: 5.13165
INFO:root:Validation iteration 180, Loss: 5.30915
INFO:root:Validation iteration 190, Loss: 5.17141
INFO:root:Validation iteration 200, Loss: 5.22427
INFO:root:Validation iteration 210, Loss: 5.30829
INFO:root:Validation iteration 220, Loss: 5.26200
INFO:root:Validation iteration 230, Loss: 5.23630
INFO:root:Validation iteration 240, Loss: 5.15579
INFO:root:Validation iteration 250, Loss: 5.20933
INFO:root:Validation iteration 260, Loss: 5.16199
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.467
INFO:root:Validation accuracy: 0.006, Validation loss: 5.18624
INFO:root:Best validation accuracy: 0.006 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 10, Loss: 5.21583
INFO:root:Validation iteration 20, Loss: 5.22695
INFO:root:Validation iteration 30, Loss: 5.22825
INFO:root:Validation iteration 40, Loss: 5.20683
INFO:root:Validation iteration 50, Loss: 5.22659
INFO:root:Validation iteration 60, Loss: 5.18180
INFO:root:Validation iteration 70, Loss: 5.11643
INFO:root:Validation iteration 80, Loss: 5.30727
INFO:root:Validation iteration 90, Loss: 5.17900
INFO:root:Validation iteration 100, Loss: 5.07457
INFO:root:Validation iteration 110, Loss: 5.16511
INFO:root:Validation iteration 120, Loss: 5.22766
INFO:root:Validation iteration 130, Loss: 5.34831
INFO:root:Validation iteration 140, Loss: 5.14659
INFO:root:Validation iteration 150, Loss: 5.09718
INFO:root:Validation iteration 160, Loss: 5.16940
INFO:root:Validation iteration 170, Loss: 5.17021
INFO:root:Validation iteration 180, Loss: 4.99913
INFO:root:Validation iteration 190, Loss: 5.25389
INFO:root:Validation iteration 200, Loss: 5.14682
INFO:root:Validation iteration 210, Loss: 5.25725
INFO:root:Validation iteration 220, Loss: 5.18313
INFO:root:Validation iteration 230, Loss: 5.10649
INFO:root:Validation iteration 240, Loss: 5.22590
INFO:root:Validation iteration 250, Loss: 5.17569
INFO:root:Validation iteration 260, Loss: 5.29557
Test accuracy: 0.006, Test loss: 5.19178
INFO:root:Saving results...
INFO:root:Done!
"""


string3 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model.pth', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 188MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 30, Loss: 5.54293
INFO:root:Training epoch 1, Iteration 60, Loss: 4.95016
INFO:root:Training epoch 1, Iteration 90, Loss: 4.91639
INFO:root:Training epoch 1, Iteration 120, Loss: 4.86598
INFO:root:Training epoch 1, Iteration 150, Loss: 4.77163
INFO:root:Training epoch 1, Iteration 180, Loss: 4.80058
INFO:root:Training epoch 1, Iteration 210, Loss: 4.72612
INFO:root:Training epoch 1, Iteration 240, Loss: 4.82566
INFO:root:Training epoch 1, Iteration 270, Loss: 4.87217
INFO:root:Training epoch 1, Iteration 300, Loss: 4.68157
INFO:root:Training epoch 1, Iteration 330, Loss: 4.69146
INFO:root:Training epoch 1, Iteration 360, Loss: 4.68678
INFO:root:Training epoch 1, Iteration 390, Loss: 4.62102
INFO:root:Training epoch 1, Iteration 420, Loss: 4.62267
INFO:root:Training epoch 1, Iteration 450, Loss: 4.67079
INFO:root:Training epoch 1, Iteration 480, Loss: 4.63895
INFO:root:Training epoch 1, Iteration 510, Loss: 4.52529
INFO:root:Training epoch 1, Iteration 540, Loss: 4.68842
INFO:root:Training epoch 1, Iteration 570, Loss: 4.71091
INFO:root:Training epoch 1, Iteration 600, Loss: 4.60669
INFO:root:Training epoch 1, Iteration 630, Loss: 4.64850
INFO:root:Training epoch 1, Iteration 660, Loss: 4.51956
INFO:root:Training epoch 1, Iteration 690, Loss: 4.60341
INFO:root:Training epoch 1, Iteration 720, Loss: 4.60900
INFO:root:Training epoch 1, Iteration 750, Loss: 4.53126
INFO:root:Training epoch 1, Iteration 780, Loss: 4.64633
INFO:root:Validation iteration 10, Loss: 134.07166
INFO:root:Validation iteration 20, Loss: 130.06226
INFO:root:Validation iteration 30, Loss: 129.93056
INFO:root:Validation iteration 40, Loss: 134.42078
INFO:root:Validation iteration 50, Loss: 134.03251
INFO:root:Validation iteration 60, Loss: 134.21034
INFO:root:Validation iteration 70, Loss: 139.00407
INFO:root:Validation iteration 80, Loss: 138.81503
INFO:root:Validation iteration 90, Loss: 146.36100
INFO:root:Validation iteration 100, Loss: 131.62881
INFO:root:Validation iteration 110, Loss: 132.74166
INFO:root:Validation iteration 120, Loss: 129.72151
INFO:root:Validation iteration 130, Loss: 139.33947
INFO:root:Validation iteration 140, Loss: 139.69878
INFO:root:Validation iteration 150, Loss: 150.33624
INFO:root:Validation iteration 160, Loss: 129.22062
INFO:root:Validation iteration 170, Loss: 142.02164
INFO:root:Validation iteration 180, Loss: 136.34818
INFO:root:Validation iteration 190, Loss: 7606.37370
INFO:root:Validation iteration 200, Loss: 143.92882
INFO:root:Validation iteration 210, Loss: 142.33458
INFO:root:Validation iteration 220, Loss: 140.42402
INFO:root:Validation iteration 230, Loss: 150.92698
INFO:root:Validation iteration 240, Loss: 135.50961
INFO:root:Validation iteration 250, Loss: 138.64611
INFO:root:Validation iteration 260, Loss: 142.80322
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.726
INFO:root:Validation accuracy: 0.006, Validation loss: 418.75933
INFO:root:Training epoch 2, Iteration 30, Loss: 4.50782
INFO:root:Training epoch 2, Iteration 60, Loss: 4.50669
INFO:root:Training epoch 2, Iteration 90, Loss: 4.55993
INFO:root:Training epoch 2, Iteration 120, Loss: 4.55067
INFO:root:Training epoch 2, Iteration 150, Loss: 4.39549
INFO:root:Training epoch 2, Iteration 180, Loss: 4.53719
INFO:root:Training epoch 2, Iteration 210, Loss: 4.49182
INFO:root:Training epoch 2, Iteration 240, Loss: 4.51428
INFO:root:Training epoch 2, Iteration 270, Loss: 4.54591
INFO:root:Training epoch 2, Iteration 300, Loss: 4.41577
INFO:root:Training epoch 2, Iteration 330, Loss: 4.54377
INFO:root:Training epoch 2, Iteration 360, Loss: 4.48792
INFO:root:Training epoch 2, Iteration 390, Loss: 4.41208
INFO:root:Training epoch 2, Iteration 420, Loss: 4.46155
INFO:root:Training epoch 2, Iteration 450, Loss: 4.42990
INFO:root:Training epoch 2, Iteration 480, Loss: 4.47298
INFO:root:Training epoch 2, Iteration 510, Loss: 4.39869
INFO:root:Training epoch 2, Iteration 540, Loss: 4.40459
INFO:root:Training epoch 2, Iteration 570, Loss: 4.21137
INFO:root:Training epoch 2, Iteration 600, Loss: 4.33883
INFO:root:Training epoch 2, Iteration 630, Loss: 4.41243
INFO:root:Training epoch 2, Iteration 660, Loss: 4.49004
INFO:root:Training epoch 2, Iteration 690, Loss: 4.41044
INFO:root:Training epoch 2, Iteration 720, Loss: 4.40507
INFO:root:Training epoch 2, Iteration 750, Loss: 4.28337
INFO:root:Training epoch 2, Iteration 780, Loss: 4.39138
INFO:root:Validation iteration 10, Loss: 5.08927
INFO:root:Validation iteration 20, Loss: 5.06259
INFO:root:Validation iteration 30, Loss: 5.02570
INFO:root:Validation iteration 40, Loss: 5.17240
INFO:root:Validation iteration 50, Loss: 5.35418
INFO:root:Validation iteration 60, Loss: 5.18233
INFO:root:Validation iteration 70, Loss: 5.37920
INFO:root:Validation iteration 80, Loss: 5.28024
INFO:root:Validation iteration 90, Loss: 5.41087
INFO:root:Validation iteration 100, Loss: 5.18127
INFO:root:Validation iteration 110, Loss: 5.19075
INFO:root:Validation iteration 120, Loss: 5.02302
INFO:root:Validation iteration 130, Loss: 5.22212
INFO:root:Validation iteration 140, Loss: 5.36866
INFO:root:Validation iteration 150, Loss: 5.57910
INFO:root:Validation iteration 160, Loss: 5.12518
INFO:root:Validation iteration 170, Loss: 5.47147
INFO:root:Validation iteration 180, Loss: 5.28812
INFO:root:Validation iteration 190, Loss: 9279.76127
INFO:root:Validation iteration 200, Loss: 5.25332
INFO:root:Validation iteration 210, Loss: 5.23735
INFO:root:Validation iteration 220, Loss: 5.27026
INFO:root:Validation iteration 230, Loss: 5.45560
INFO:root:Validation iteration 240, Loss: 5.27337
INFO:root:Validation iteration 250, Loss: 5.21998
INFO:root:Validation iteration 260, Loss: 5.45676
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.445
INFO:root:Validation accuracy: 0.006, Validation loss: 353.93487
INFO:root:Best validation accuracy: 0.006 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 10, Loss: 5.12517
INFO:root:Validation iteration 20, Loss: 5.26679
INFO:root:Validation iteration 30, Loss: 5.31261
INFO:root:Validation iteration 40, Loss: 5.31260
INFO:root:Validation iteration 50, Loss: 5.26350
INFO:root:Validation iteration 60, Loss: 5.26321
INFO:root:Validation iteration 70, Loss: 5.23060
INFO:root:Validation iteration 80, Loss: 5.23880
INFO:root:Validation iteration 90, Loss: 5.09323
INFO:root:Validation iteration 100, Loss: 5.34076
INFO:root:Validation iteration 110, Loss: 5.17657
INFO:root:Validation iteration 120, Loss: 5.30248
INFO:root:Validation iteration 130, Loss: 5.36077
INFO:root:Validation iteration 140, Loss: 5.35179
INFO:root:Validation iteration 150, Loss: 5.38405
INFO:root:Validation iteration 160, Loss: 5.10685
INFO:root:Validation iteration 170, Loss: 5.24026
INFO:root:Validation iteration 180, Loss: 5.26084
INFO:root:Validation iteration 190, Loss: 5.25115
INFO:root:Validation iteration 200, Loss: 5.41489
INFO:root:Validation iteration 210, Loss: 5.15493
INFO:root:Validation iteration 220, Loss: 5.15444
INFO:root:Validation iteration 230, Loss: 5.28846
INFO:root:Validation iteration 240, Loss: 5.23210
INFO:root:Validation iteration 250, Loss: 5.16952
INFO:root:Validation iteration 260, Loss: 5.23477
Test accuracy: 0.006, Test loss: 5.25832
INFO:root:Saving results...
INFO:root:Done!
"""

string4 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model.pth', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=True, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 176MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 30, Loss: 5.47458
INFO:root:Training epoch 1, Iteration 60, Loss: 4.98530
INFO:root:Training epoch 1, Iteration 90, Loss: 4.94258
INFO:root:Training epoch 1, Iteration 120, Loss: 4.88419
INFO:root:Training epoch 1, Iteration 150, Loss: 4.90662
INFO:root:Training epoch 1, Iteration 180, Loss: 4.89445
INFO:root:Training epoch 1, Iteration 210, Loss: 4.82092
INFO:root:Training epoch 1, Iteration 240, Loss: 4.78569
INFO:root:Training epoch 1, Iteration 270, Loss: 4.76113
INFO:root:Training epoch 1, Iteration 300, Loss: 4.75981
INFO:root:Training epoch 1, Iteration 330, Loss: 4.78825
INFO:root:Training epoch 1, Iteration 360, Loss: 4.74982
INFO:root:Training epoch 1, Iteration 390, Loss: 4.71627
INFO:root:Training epoch 1, Iteration 420, Loss: 4.63573
INFO:root:Training epoch 1, Iteration 450, Loss: 4.64995
INFO:root:Training epoch 1, Iteration 480, Loss: 4.57376
INFO:root:Training epoch 1, Iteration 510, Loss: 4.66776
INFO:root:Training epoch 1, Iteration 540, Loss: 4.68246
INFO:root:Training epoch 1, Iteration 570, Loss: 4.62166
INFO:root:Training epoch 1, Iteration 600, Loss: 4.76247
INFO:root:Training epoch 1, Iteration 630, Loss: 4.79620
INFO:root:Training epoch 1, Iteration 660, Loss: 4.71972
INFO:root:Training epoch 1, Iteration 690, Loss: 4.72722
INFO:root:Training epoch 1, Iteration 720, Loss: 4.84156
INFO:root:Training epoch 1, Iteration 750, Loss: 4.76565
INFO:root:Training epoch 1, Iteration 780, Loss: 4.77616
INFO:root:Validation iteration 10, Loss: 4.75821
INFO:root:Validation iteration 20, Loss: 4.67643
INFO:root:Validation iteration 30, Loss: 4.72697
INFO:root:Validation iteration 40, Loss: 4.59212
INFO:root:Validation iteration 50, Loss: 4.75501
INFO:root:Validation iteration 60, Loss: 4.60345
INFO:root:Validation iteration 70, Loss: 4.85324
INFO:root:Validation iteration 80, Loss: 4.71759
INFO:root:Validation iteration 90, Loss: 4.88779
INFO:root:Validation iteration 100, Loss: 4.72114
INFO:root:Validation iteration 110, Loss: 4.69868
INFO:root:Validation iteration 120, Loss: 4.53785
INFO:root:Validation iteration 130, Loss: 4.77439
INFO:root:Validation iteration 140, Loss: 4.81928
INFO:root:Validation iteration 150, Loss: 4.89070
INFO:root:Validation iteration 160, Loss: 4.70215
INFO:root:Validation iteration 170, Loss: 4.79422
INFO:root:Validation iteration 180, Loss: 4.73291
INFO:root:Validation iteration 190, Loss: 4.59838
INFO:root:Validation iteration 200, Loss: 4.73889
INFO:root:Validation iteration 210, Loss: 4.80878
INFO:root:Validation iteration 220, Loss: 4.78027
INFO:root:Validation iteration 230, Loss: 4.96646
INFO:root:Validation iteration 240, Loss: 4.80917
INFO:root:Validation iteration 250, Loss: 4.81447
INFO:root:Validation iteration 260, Loss: 4.80557
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.794
INFO:root:Validation accuracy: 0.009, Validation loss: 4.75429
INFO:root:Training epoch 2, Iteration 30, Loss: 4.73930
INFO:root:Training epoch 2, Iteration 60, Loss: 4.71187
INFO:root:Training epoch 2, Iteration 90, Loss: 4.63591
INFO:root:Training epoch 2, Iteration 120, Loss: 4.57511
INFO:root:Training epoch 2, Iteration 150, Loss: 4.63618
INFO:root:Training epoch 2, Iteration 180, Loss: 4.70980
INFO:root:Training epoch 2, Iteration 210, Loss: 4.66342
INFO:root:Training epoch 2, Iteration 240, Loss: 4.63391
INFO:root:Training epoch 2, Iteration 270, Loss: 4.62521
INFO:root:Training epoch 2, Iteration 300, Loss: 4.64069
INFO:root:Training epoch 2, Iteration 330, Loss: 4.60135
INFO:root:Training epoch 2, Iteration 360, Loss: 4.56955
INFO:root:Training epoch 2, Iteration 390, Loss: 4.63157
INFO:root:Training epoch 2, Iteration 420, Loss: 4.66256
INFO:root:Training epoch 2, Iteration 450, Loss: 4.61399
INFO:root:Training epoch 2, Iteration 480, Loss: 4.61403
INFO:root:Training epoch 2, Iteration 510, Loss: 4.56000
INFO:root:Training epoch 2, Iteration 540, Loss: 4.58404
INFO:root:Training epoch 2, Iteration 570, Loss: 4.59716
INFO:root:Training epoch 2, Iteration 600, Loss: 4.53919
INFO:root:Training epoch 2, Iteration 630, Loss: 4.62992
INFO:root:Training epoch 2, Iteration 660, Loss: 4.58989
INFO:root:Training epoch 2, Iteration 690, Loss: 4.53766
INFO:root:Training epoch 2, Iteration 720, Loss: 4.60452
INFO:root:Training epoch 2, Iteration 750, Loss: 4.60048
INFO:root:Training epoch 2, Iteration 780, Loss: 4.65628
INFO:root:Validation iteration 10, Loss: 4.81345
INFO:root:Validation iteration 20, Loss: 4.78700
INFO:root:Validation iteration 30, Loss: 4.73815
INFO:root:Validation iteration 40, Loss: 4.72911
INFO:root:Validation iteration 50, Loss: 4.81474
INFO:root:Validation iteration 60, Loss: 4.66817
INFO:root:Validation iteration 70, Loss: 4.82975
INFO:root:Validation iteration 80, Loss: 4.72639
INFO:root:Validation iteration 90, Loss: 4.84574
INFO:root:Validation iteration 100, Loss: 4.81867
INFO:root:Validation iteration 110, Loss: 4.72887
INFO:root:Validation iteration 120, Loss: 4.71948
INFO:root:Validation iteration 130, Loss: 4.82718
INFO:root:Validation iteration 140, Loss: 4.83846
INFO:root:Validation iteration 150, Loss: 4.97280
INFO:root:Validation iteration 160, Loss: 4.74474
INFO:root:Validation iteration 170, Loss: 4.82705
INFO:root:Validation iteration 180, Loss: 4.88032
INFO:root:Validation iteration 190, Loss: 4.72610
INFO:root:Validation iteration 200, Loss: 4.76336
INFO:root:Validation iteration 210, Loss: 4.88842
INFO:root:Validation iteration 220, Loss: 4.78598
INFO:root:Validation iteration 230, Loss: 4.90082
INFO:root:Validation iteration 240, Loss: 4.84226
INFO:root:Validation iteration 250, Loss: 4.78717
INFO:root:Validation iteration 260, Loss: 4.77194
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.622
INFO:root:Validation accuracy: 0.008, Validation loss: 4.79804
INFO:root:Best validation accuracy: 0.009 at epoch 1
INFO:root:Inference...
INFO:root:Validation iteration 10, Loss: 4.72461
INFO:root:Validation iteration 20, Loss: 4.79525
INFO:root:Validation iteration 30, Loss: 4.81253
INFO:root:Validation iteration 40, Loss: 4.74058
INFO:root:Validation iteration 50, Loss: 4.83146
INFO:root:Validation iteration 60, Loss: 4.80571
INFO:root:Validation iteration 70, Loss: 4.74798
INFO:root:Validation iteration 80, Loss: 4.86108
INFO:root:Validation iteration 90, Loss: 4.73233
INFO:root:Validation iteration 100, Loss: 4.80306
INFO:root:Validation iteration 110, Loss: 4.75472
INFO:root:Validation iteration 120, Loss: 4.71215
INFO:root:Validation iteration 130, Loss: 4.89686
INFO:root:Validation iteration 140, Loss: 4.77821
INFO:root:Validation iteration 150, Loss: 4.77382
INFO:root:Validation iteration 160, Loss: 4.73050
INFO:root:Validation iteration 170, Loss: 4.74704
INFO:root:Validation iteration 180, Loss: 4.75605
INFO:root:Validation iteration 190, Loss: 4.61505
INFO:root:Validation iteration 200, Loss: 4.78751
INFO:root:Validation iteration 210, Loss: 4.75237
INFO:root:Validation iteration 220, Loss: 4.68701
INFO:root:Validation iteration 230, Loss: 4.86157
INFO:root:Validation iteration 240, Loss: 4.80229
INFO:root:Validation iteration 250, Loss: 4.67232
INFO:root:Validation iteration 260, Loss: 4.81810
Test accuracy: 0.009, Test loss: 4.76954
INFO:root:Saving results...
INFO:root:Done!
"""


string5 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model.pth', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=True), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=True, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4758678078651428, 0.42080211639404297, 0.3604283332824707], 'std': [0.2790554165840149, 0.2741965651512146, 0.2640019357204437], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4758678078651428, 0.42080211639404297, 0.3604283332824707], std=[0.2790554165840149, 0.2741965651512146, 0.2640019357204437])']}}}
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 180MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Validation iteration 1, Loss: 5.08696
INFO:root:Validation iteration 10, Loss: 5.08421
INFO:root:Validation iteration 20, Loss: 5.08689
INFO:root:Validation iteration 30, Loss: 5.08124
INFO:root:Validation iteration 40, Loss: 5.08410
INFO:root:Validation iteration 50, Loss: 5.08523
INFO:root:Validation iteration 60, Loss: 5.08233
INFO:root:Validation iteration 70, Loss: 5.08715
INFO:root:Validation iteration 80, Loss: 5.07977
INFO:root:Validation iteration 90, Loss: 5.08806
INFO:root:Validation iteration 100, Loss: 5.08795
INFO:root:Validation iteration 110, Loss: 5.08297
INFO:root:Validation iteration 120, Loss: 5.08647
INFO:root:Validation iteration 130, Loss: 5.08408
INFO:root:Validation iteration 140, Loss: 5.08253
INFO:root:Validation iteration 150, Loss: 5.08305
INFO:root:Validation iteration 160, Loss: 5.08122
INFO:root:Validation iteration 170, Loss: 5.08599
INFO:root:Validation iteration 180, Loss: 5.08392
INFO:root:Validation iteration 190, Loss: 5.08773
INFO:root:Validation iteration 200, Loss: 5.08797
INFO:root:Validation iteration 210, Loss: 5.08661
INFO:root:Validation iteration 220, Loss: 5.08446
INFO:root:Validation iteration 230, Loss: 5.08464
INFO:root:Validation iteration 240, Loss: 5.08575
INFO:root:Validation iteration 250, Loss: 5.08291
INFO:root:Validation iteration 260, Loss: 5.08452
INFO:root:Validation iteration 270, Loss: 5.08813
INFO:root:Validation iteration 280, Loss: 5.08209
INFO:root:Validation iteration 290, Loss: 5.08417
INFO:root:Validation iteration 300, Loss: 5.08693
INFO:root:Validation iteration 310, Loss: 5.08238
INFO:root:Validation iteration 320, Loss: 5.08517
INFO:root:Validation iteration 330, Loss: 5.08326
INFO:root:Validation iteration 340, Loss: 5.08237
INFO:root:Validation iteration 350, Loss: 5.08611
INFO:root:Validation iteration 360, Loss: 5.08574
INFO:root:Validation iteration 370, Loss: 5.08515
INFO:root:Validation iteration 380, Loss: 5.08894
INFO:root:Validation iteration 390, Loss: 5.08061
INFO:root:Validation iteration 400, Loss: 5.08915
INFO:root:Validation iteration 410, Loss: 5.08306
INFO:root:Validation iteration 420, Loss: 5.08565
INFO:root:Validation iteration 430, Loss: 5.08449
INFO:root:Validation iteration 440, Loss: 5.08572
INFO:root:Validation iteration 450, Loss: 5.08386
INFO:root:Validation iteration 460, Loss: 5.08536
INFO:root:Validation iteration 470, Loss: 5.08080
INFO:root:Validation iteration 480, Loss: 5.08141
INFO:root:Validation iteration 490, Loss: 5.08871
INFO:root:Validation iteration 500, Loss: 5.08887
INFO:root:Validation iteration 510, Loss: 5.08468
INFO:root:Validation iteration 520, Loss: 5.08358
INFO:root:Validation iteration 530, Loss: 5.09003
INFO:root:Validation iteration 540, Loss: 5.08647
INFO:root:Validation iteration 550, Loss: 5.09031
INFO:root:Validation iteration 560, Loss: 5.08981
INFO:root:Validation iteration 570, Loss: 5.09175
INFO:root:Validation iteration 580, Loss: 5.08758
INFO:root:Validation iteration 590, Loss: 5.08337
INFO:root:Validation iteration 600, Loss: 5.08627
INFO:root:Validation iteration 610, Loss: 5.08645
INFO:root:Validation iteration 620, Loss: 5.08780
INFO:root:Validation iteration 630, Loss: 5.08377
INFO:root:Validation iteration 640, Loss: 5.08460
INFO:root:Validation iteration 650, Loss: 5.07982
INFO:root:Validation iteration 660, Loss: 5.08329
INFO:root:Validation iteration 670, Loss: 5.07900
INFO:root:Validation iteration 680, Loss: 5.08386
INFO:root:Validation iteration 690, Loss: 5.08644
INFO:root:Validation iteration 700, Loss: 5.08163
INFO:root:Validation iteration 710, Loss: 5.08665
INFO:root:Validation iteration 720, Loss: 5.08532
INFO:root:Validation iteration 730, Loss: 5.08851
INFO:root:Validation iteration 740, Loss: 5.08948
INFO:root:Validation iteration 750, Loss: 5.08397
INFO:root:Validation iteration 760, Loss: 5.08530
INFO:root:Validation iteration 770, Loss: 5.08845
INFO:root:Validation iteration 780, Loss: 5.08758
INFO:root:Validation iteration 790, Loss: 5.08796
INFO:root:Validation iteration 1, Loss: 5.07670
INFO:root:Validation iteration 10, Loss: 5.08580
INFO:root:Validation iteration 20, Loss: 5.08922
INFO:root:Validation iteration 30, Loss: 5.08552
INFO:root:Validation iteration 40, Loss: 5.08740
INFO:root:Validation iteration 50, Loss: 5.09028
INFO:root:Validation iteration 60, Loss: 5.08781
INFO:root:Validation iteration 70, Loss: 5.09152
INFO:root:Validation iteration 80, Loss: 5.08744
INFO:root:Validation iteration 90, Loss: 5.08544
INFO:root:Validation iteration 100, Loss: 5.08493
INFO:root:Validation iteration 110, Loss: 5.09137
INFO:root:Validation iteration 120, Loss: 5.09305
INFO:root:Validation iteration 130, Loss: 5.08109
INFO:root:Validation iteration 140, Loss: 5.08029
INFO:root:Validation iteration 150, Loss: 5.08038
INFO:root:Validation iteration 160, Loss: 5.08256
INFO:root:Validation iteration 170, Loss: 5.08007
INFO:root:Validation iteration 180, Loss: 5.08268
INFO:root:Validation iteration 190, Loss: 5.08479
INFO:root:Validation iteration 200, Loss: 5.07895
INFO:root:Validation iteration 210, Loss: 5.08451
INFO:root:Validation iteration 220, Loss: 5.08323
INFO:root:Validation iteration 230, Loss: 5.08176
INFO:root:Validation iteration 240, Loss: 5.08441
INFO:root:Validation iteration 250, Loss: 5.08433
INFO:root:Validation iteration 260, Loss: 5.08758
INFO:root:Sanity check - Before training
INFO:root:Training loss: 5.085
INFO:root:Validation accuracy: 0.008, Validation loss: 5.08530
INFO:root:Training epoch 1, Iteration 1, Loss: 5.21682
INFO:root:Training epoch 1, Iteration 30, Loss: 5.06561
INFO:root:Training epoch 1, Iteration 60, Loss: 4.90139
INFO:root:Training epoch 1, Iteration 90, Loss: 4.94778
INFO:root:Training epoch 1, Iteration 120, Loss: 4.76091
INFO:root:Training epoch 1, Iteration 150, Loss: 4.67033
INFO:root:Training epoch 1, Iteration 180, Loss: 4.74974
INFO:root:Training epoch 1, Iteration 210, Loss: 4.69027
INFO:root:Training epoch 1, Iteration 240, Loss: 4.59096
INFO:root:Training epoch 1, Iteration 270, Loss: 4.63440
INFO:root:Training epoch 1, Iteration 300, Loss: 4.42636
INFO:root:Training epoch 1, Iteration 330, Loss: 4.62613
INFO:root:Training epoch 1, Iteration 360, Loss: 4.43964
INFO:root:Training epoch 1, Iteration 390, Loss: 4.41716
INFO:root:Training epoch 1, Iteration 420, Loss: 4.47939
INFO:root:Training epoch 1, Iteration 450, Loss: 4.48613
INFO:root:Training epoch 1, Iteration 480, Loss: 4.47046
INFO:root:Training epoch 1, Iteration 510, Loss: 4.49993
INFO:root:Training epoch 1, Iteration 540, Loss: 4.38889
INFO:root:Training epoch 1, Iteration 570, Loss: 4.36949
INFO:root:Training epoch 1, Iteration 600, Loss: 4.27264
INFO:root:Training epoch 1, Iteration 630, Loss: 4.33628
INFO:root:Training epoch 1, Iteration 660, Loss: 4.33236
INFO:root:Training epoch 1, Iteration 690, Loss: 4.41075
INFO:root:Training epoch 1, Iteration 720, Loss: 4.36536
INFO:root:Training epoch 1, Iteration 750, Loss: 4.25569
INFO:root:Training epoch 1, Iteration 780, Loss: 4.32947
INFO:root:Validation iteration 1, Loss: 3.47547
INFO:root:Validation iteration 10, Loss: 4.39174
INFO:root:Validation iteration 20, Loss: 4.54188
INFO:root:Validation iteration 30, Loss: 4.34248
INFO:root:Validation iteration 40, Loss: 4.61950
INFO:root:Validation iteration 50, Loss: 4.65924
INFO:root:Validation iteration 60, Loss: 4.07348
INFO:root:Validation iteration 70, Loss: 4.68897
INFO:root:Validation iteration 80, Loss: 4.24052
INFO:root:Validation iteration 90, Loss: 4.54051
INFO:root:Validation iteration 100, Loss: 4.46584
INFO:root:Validation iteration 110, Loss: 4.24098
INFO:root:Validation iteration 120, Loss: 4.65687
INFO:root:Validation iteration 130, Loss: 4.57393
INFO:root:Validation iteration 140, Loss: 4.45304
INFO:root:Validation iteration 150, Loss: 4.81028
INFO:root:Validation iteration 160, Loss: 4.44666
INFO:root:Validation iteration 170, Loss: 4.47109
INFO:root:Validation iteration 180, Loss: 4.78440
INFO:root:Validation iteration 190, Loss: 4.55709
INFO:root:Validation iteration 200, Loss: 4.25113
INFO:root:Validation iteration 210, Loss: 4.53120
INFO:root:Validation iteration 220, Loss: 4.33942
INFO:root:Validation iteration 230, Loss: 4.49178
INFO:root:Validation iteration 240, Loss: 5.13502
INFO:root:Validation iteration 250, Loss: 4.88565
INFO:root:Validation iteration 260, Loss: 4.48791
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.530
INFO:root:Validation accuracy: 0.034, Validation loss: 4.54127
INFO:root:Training epoch 2, Iteration 1, Loss: 3.95966
INFO:root:Training epoch 2, Iteration 30, Loss: 4.19258
INFO:root:Training epoch 2, Iteration 60, Loss: 4.08634
INFO:root:Training epoch 2, Iteration 90, Loss: 4.20495
INFO:root:Training epoch 2, Iteration 120, Loss: 4.21560
INFO:root:Training epoch 2, Iteration 150, Loss: 4.04809
INFO:root:Training epoch 2, Iteration 180, Loss: 4.17540
INFO:root:Training epoch 2, Iteration 210, Loss: 4.17080
INFO:root:Training epoch 2, Iteration 240, Loss: 4.12296
INFO:root:Training epoch 2, Iteration 270, Loss: 4.17881
INFO:root:Training epoch 2, Iteration 300, Loss: 4.13432
INFO:root:Training epoch 2, Iteration 330, Loss: 4.04558
INFO:root:Training epoch 2, Iteration 360, Loss: 4.11809
INFO:root:Training epoch 2, Iteration 390, Loss: 4.15297
INFO:root:Training epoch 2, Iteration 420, Loss: 4.10761
INFO:root:Training epoch 2, Iteration 450, Loss: 4.09353
INFO:root:Training epoch 2, Iteration 480, Loss: 4.14550
INFO:root:Training epoch 2, Iteration 510, Loss: 4.10474
INFO:root:Training epoch 2, Iteration 540, Loss: 4.06108
INFO:root:Training epoch 2, Iteration 570, Loss: 4.05812
INFO:root:Training epoch 2, Iteration 600, Loss: 4.02028
INFO:root:Training epoch 2, Iteration 630, Loss: 4.00287
INFO:root:Training epoch 2, Iteration 660, Loss: 3.97008
INFO:root:Training epoch 2, Iteration 690, Loss: 4.10361
INFO:root:Training epoch 2, Iteration 720, Loss: 4.08244
INFO:root:Training epoch 2, Iteration 750, Loss: 3.97152
INFO:root:Training epoch 2, Iteration 780, Loss: 3.89920
INFO:root:Validation iteration 1, Loss: 3.18450
INFO:root:Validation iteration 10, Loss: 5.87068
INFO:root:Validation iteration 20, Loss: 3.78366
INFO:root:Validation iteration 30, Loss: 4.68787
INFO:root:Validation iteration 40, Loss: 4.50244
INFO:root:Validation iteration 50, Loss: 4.20081
INFO:root:Validation iteration 60, Loss: 3.88074
INFO:root:Validation iteration 70, Loss: 4.95957
INFO:root:Validation iteration 80, Loss: 3.99986
INFO:root:Validation iteration 90, Loss: 4.12793
INFO:root:Validation iteration 100, Loss: 5.37613
INFO:root:Validation iteration 110, Loss: 4.54738
INFO:root:Validation iteration 120, Loss: 5.59063
INFO:root:Validation iteration 130, Loss: 4.62548
INFO:root:Validation iteration 140, Loss: 5.87296
INFO:root:Validation iteration 150, Loss: 4.42377
INFO:root:Validation iteration 160, Loss: 4.26011
INFO:root:Validation iteration 170, Loss: 4.91403
INFO:root:Validation iteration 180, Loss: 4.09681
INFO:root:Validation iteration 190, Loss: 3.76883
INFO:root:Validation iteration 200, Loss: 4.71068
INFO:root:Validation iteration 210, Loss: 6.18629
INFO:root:Validation iteration 220, Loss: 5.26008
INFO:root:Validation iteration 230, Loss: 5.74463
INFO:root:Validation iteration 240, Loss: 4.85748
INFO:root:Validation iteration 250, Loss: 4.33440
INFO:root:Validation iteration 260, Loss: 4.75830
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.093
INFO:root:Validation accuracy: 0.055, Validation loss: 4.76057
INFO:root:Best validation accuracy: 0.055 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.81771
INFO:root:Validation iteration 10, Loss: 5.96355
INFO:root:Validation iteration 20, Loss: 4.38529
INFO:root:Validation iteration 30, Loss: 4.61127
INFO:root:Validation iteration 40, Loss: 5.23026
INFO:root:Validation iteration 50, Loss: 5.27708
INFO:root:Validation iteration 60, Loss: 3.92303
INFO:root:Validation iteration 70, Loss: 5.04456
INFO:root:Validation iteration 80, Loss: 5.40223
INFO:root:Validation iteration 90, Loss: 4.97651
INFO:root:Validation iteration 100, Loss: 5.16332
INFO:root:Validation iteration 110, Loss: 5.39729
INFO:root:Validation iteration 120, Loss: 5.86484
INFO:root:Validation iteration 130, Loss: 5.65286
INFO:root:Validation iteration 140, Loss: 6.28023
INFO:root:Validation iteration 150, Loss: 6.69450
INFO:root:Validation iteration 160, Loss: 4.11470
INFO:root:Validation iteration 170, Loss: 5.65435
INFO:root:Validation iteration 180, Loss: 4.40241
INFO:root:Validation iteration 190, Loss: 4.40857
INFO:root:Validation iteration 200, Loss: 5.44968
INFO:root:Validation iteration 210, Loss: 4.34527
INFO:root:Validation iteration 220, Loss: 5.44978
INFO:root:Validation iteration 230, Loss: 4.00909
INFO:root:Validation iteration 240, Loss: 4.27344
INFO:root:Validation iteration 250, Loss: 3.80511
INFO:root:Validation iteration 260, Loss: 4.47865
Test accuracy: 0.051, Test loss: 5.01489
INFO:root:Saving results...
INFO:root:Done!
"""

string6 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model.pth', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=True), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4758678078651428, 0.42080211639404297, 0.3604283332824707], 'std': [0.2790554165840149, 0.2741965651512146, 0.2640019357204437], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4758678078651428, 0.42080211639404297, 0.3604283332824707], std=[0.2790554165840149, 0.2741965651512146, 0.2640019357204437])']}}}
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 179MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Validation iteration 1, Loss: 5.08766
INFO:root:Validation iteration 10, Loss: 5.08132
INFO:root:Validation iteration 20, Loss: 5.08148
INFO:root:Validation iteration 30, Loss: 5.08223
INFO:root:Validation iteration 40, Loss: 5.08188
INFO:root:Validation iteration 50, Loss: 5.08119
INFO:root:Validation iteration 60, Loss: 5.08100
INFO:root:Validation iteration 70, Loss: 5.08216
INFO:root:Validation iteration 80, Loss: 5.08144
INFO:root:Validation iteration 90, Loss: 5.08064
INFO:root:Validation iteration 100, Loss: 5.08153
INFO:root:Validation iteration 110, Loss: 5.08118
INFO:root:Validation iteration 120, Loss: 5.08245
INFO:root:Validation iteration 130, Loss: 5.08240
INFO:root:Validation iteration 140, Loss: 5.08278
INFO:root:Validation iteration 150, Loss: 5.08090
INFO:root:Validation iteration 160, Loss: 5.08263
INFO:root:Validation iteration 170, Loss: 5.08283
INFO:root:Validation iteration 180, Loss: 5.08224
INFO:root:Validation iteration 190, Loss: 5.08037
INFO:root:Validation iteration 200, Loss: 5.08105
INFO:root:Validation iteration 210, Loss: 5.08322
INFO:root:Validation iteration 220, Loss: 5.08300
INFO:root:Validation iteration 230, Loss: 5.08238
INFO:root:Validation iteration 240, Loss: 5.08047
INFO:root:Validation iteration 250, Loss: 5.08131
INFO:root:Validation iteration 260, Loss: 5.08304
INFO:root:Validation iteration 270, Loss: 5.08304
INFO:root:Validation iteration 280, Loss: 5.08068
INFO:root:Validation iteration 290, Loss: 5.08309
INFO:root:Validation iteration 300, Loss: 5.08267
INFO:root:Validation iteration 310, Loss: 5.07983
INFO:root:Validation iteration 320, Loss: 5.08146
INFO:root:Validation iteration 330, Loss: 5.08253
INFO:root:Validation iteration 340, Loss: 5.08246
INFO:root:Validation iteration 350, Loss: 5.08299
INFO:root:Validation iteration 360, Loss: 5.08128
INFO:root:Validation iteration 370, Loss: 5.08366
INFO:root:Validation iteration 380, Loss: 5.08306
INFO:root:Validation iteration 390, Loss: 5.08108
INFO:root:Validation iteration 400, Loss: 5.08084
INFO:root:Validation iteration 410, Loss: 5.08175
INFO:root:Validation iteration 420, Loss: 5.08138
INFO:root:Validation iteration 430, Loss: 5.08305
INFO:root:Validation iteration 440, Loss: 5.08273
INFO:root:Validation iteration 450, Loss: 5.08383
INFO:root:Validation iteration 460, Loss: 5.08266
INFO:root:Validation iteration 470, Loss: 5.08135
INFO:root:Validation iteration 480, Loss: 5.08078
INFO:root:Validation iteration 490, Loss: 5.08326
INFO:root:Validation iteration 500, Loss: 5.08123
INFO:root:Validation iteration 510, Loss: 5.08059
INFO:root:Validation iteration 520, Loss: 5.08195
INFO:root:Validation iteration 530, Loss: 5.08237
INFO:root:Validation iteration 540, Loss: 5.08073
INFO:root:Validation iteration 550, Loss: 5.08216
INFO:root:Validation iteration 560, Loss: 5.08125
INFO:root:Validation iteration 570, Loss: 5.08233
INFO:root:Validation iteration 580, Loss: 5.08193
INFO:root:Validation iteration 590, Loss: 5.08060
INFO:root:Validation iteration 600, Loss: 5.08168
INFO:root:Validation iteration 610, Loss: 5.08378
INFO:root:Validation iteration 620, Loss: 5.08223
INFO:root:Validation iteration 630, Loss: 5.08520
INFO:root:Validation iteration 640, Loss: 5.08138
INFO:root:Validation iteration 650, Loss: 5.08278
INFO:root:Validation iteration 660, Loss: 5.08167
INFO:root:Validation iteration 670, Loss: 5.08098
INFO:root:Validation iteration 680, Loss: 5.08325
INFO:root:Validation iteration 690, Loss: 5.08376
INFO:root:Validation iteration 700, Loss: 5.08324
INFO:root:Validation iteration 710, Loss: 5.08312
INFO:root:Validation iteration 720, Loss: 5.08215
INFO:root:Validation iteration 730, Loss: 5.08243
INFO:root:Validation iteration 740, Loss: 5.08126
INFO:root:Validation iteration 750, Loss: 5.08210
INFO:root:Validation iteration 760, Loss: 5.08424
INFO:root:Validation iteration 770, Loss: 5.08107
INFO:root:Validation iteration 780, Loss: 5.08017
INFO:root:Validation iteration 790, Loss: 5.08147
INFO:root:Validation iteration 1, Loss: 5.08396
INFO:root:Validation iteration 10, Loss: 5.08166
INFO:root:Validation iteration 20, Loss: 5.08233
INFO:root:Validation iteration 30, Loss: 5.08070
INFO:root:Validation iteration 40, Loss: 5.08209
INFO:root:Validation iteration 50, Loss: 5.08261
INFO:root:Validation iteration 60, Loss: 5.08198
INFO:root:Validation iteration 70, Loss: 5.08243
INFO:root:Validation iteration 80, Loss: 5.08139
INFO:root:Validation iteration 90, Loss: 5.08214
INFO:root:Validation iteration 100, Loss: 5.08116
INFO:root:Validation iteration 110, Loss: 5.08213
INFO:root:Validation iteration 120, Loss: 5.08223
INFO:root:Validation iteration 130, Loss: 5.08111
INFO:root:Validation iteration 140, Loss: 5.08380
INFO:root:Validation iteration 150, Loss: 5.08142
INFO:root:Validation iteration 160, Loss: 5.08142
INFO:root:Validation iteration 170, Loss: 5.08311
INFO:root:Validation iteration 180, Loss: 5.08163
INFO:root:Validation iteration 190, Loss: 5.08258
INFO:root:Validation iteration 200, Loss: 5.08135
INFO:root:Validation iteration 210, Loss: 5.08118
INFO:root:Validation iteration 220, Loss: 5.08186
INFO:root:Validation iteration 230, Loss: 5.08287
INFO:root:Validation iteration 240, Loss: 5.08117
INFO:root:Validation iteration 250, Loss: 5.08255
INFO:root:Validation iteration 260, Loss: 5.08243
INFO:root:Sanity check - Before training
INFO:root:Training loss: 5.082
INFO:root:Validation accuracy: 0.005, Validation loss: 5.08195
INFO:root:Training epoch 1, Iteration 1, Loss: 5.04869
INFO:root:Training epoch 1, Iteration 30, Loss: 5.10312
INFO:root:Training epoch 1, Iteration 60, Loss: 4.97980
INFO:root:Training epoch 1, Iteration 90, Loss: 4.87984
INFO:root:Training epoch 1, Iteration 120, Loss: 4.75548
INFO:root:Training epoch 1, Iteration 150, Loss: 4.79635
INFO:root:Training epoch 1, Iteration 180, Loss: 4.58087
INFO:root:Training epoch 1, Iteration 210, Loss: 4.57474
INFO:root:Training epoch 1, Iteration 240, Loss: 4.67832
INFO:root:Training epoch 1, Iteration 270, Loss: 4.58105
INFO:root:Training epoch 1, Iteration 300, Loss: 4.57149
INFO:root:Training epoch 1, Iteration 330, Loss: 4.51261
INFO:root:Training epoch 1, Iteration 360, Loss: 4.52839
INFO:root:Training epoch 1, Iteration 390, Loss: 4.42844
INFO:root:Training epoch 1, Iteration 420, Loss: 4.48212
INFO:root:Training epoch 1, Iteration 450, Loss: 4.50731
INFO:root:Training epoch 1, Iteration 480, Loss: 4.38642
INFO:root:Training epoch 1, Iteration 510, Loss: 4.45321
INFO:root:Training epoch 1, Iteration 540, Loss: 4.36533
INFO:root:Training epoch 1, Iteration 570, Loss: 4.37615
INFO:root:Training epoch 1, Iteration 600, Loss: 4.38795
INFO:root:Training epoch 1, Iteration 630, Loss: 4.42252
INFO:root:Training epoch 1, Iteration 660, Loss: 4.34948
INFO:root:Training epoch 1, Iteration 690, Loss: 4.33303
INFO:root:Training epoch 1, Iteration 720, Loss: 4.23917
INFO:root:Training epoch 1, Iteration 750, Loss: 4.15678
INFO:root:Training epoch 1, Iteration 780, Loss: 4.29051
INFO:root:Validation iteration 1, Loss: 3.28949
INFO:root:Validation iteration 10, Loss: 4.15800
INFO:root:Validation iteration 20, Loss: 4.04079
INFO:root:Validation iteration 30, Loss: 4.16611
INFO:root:Validation iteration 40, Loss: 4.01773
INFO:root:Validation iteration 50, Loss: 4.25641
INFO:root:Validation iteration 60, Loss: 4.06925
INFO:root:Validation iteration 70, Loss: 4.37176
INFO:root:Validation iteration 80, Loss: 4.00739
INFO:root:Validation iteration 90, Loss: 4.33181
INFO:root:Validation iteration 100, Loss: 4.39180
INFO:root:Validation iteration 110, Loss: 4.13708
INFO:root:Validation iteration 120, Loss: 4.15102
INFO:root:Validation iteration 130, Loss: 4.13207
INFO:root:Validation iteration 140, Loss: 4.29577
INFO:root:Validation iteration 150, Loss: 4.52601
INFO:root:Validation iteration 160, Loss: 4.12896
INFO:root:Validation iteration 170, Loss: 4.26953
INFO:root:Validation iteration 180, Loss: 4.38761
INFO:root:Validation iteration 190, Loss: 4.10722
INFO:root:Validation iteration 200, Loss: 4.15583
INFO:root:Validation iteration 210, Loss: 4.36498
INFO:root:Validation iteration 220, Loss: 4.19181
INFO:root:Validation iteration 230, Loss: 4.35329
INFO:root:Validation iteration 240, Loss: 4.38379
INFO:root:Validation iteration 250, Loss: 4.30637
INFO:root:Validation iteration 260, Loss: 4.30284
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.522
INFO:root:Validation accuracy: 0.042, Validation loss: 4.23136
INFO:root:Training epoch 2, Iteration 1, Loss: 4.37643
INFO:root:Training epoch 2, Iteration 30, Loss: 4.09737
INFO:root:Training epoch 2, Iteration 60, Loss: 4.09052
INFO:root:Training epoch 2, Iteration 90, Loss: 4.20501
INFO:root:Training epoch 2, Iteration 120, Loss: 4.15345
INFO:root:Training epoch 2, Iteration 150, Loss: 4.27585
INFO:root:Training epoch 2, Iteration 180, Loss: 4.12149
INFO:root:Training epoch 2, Iteration 210, Loss: 4.19251
INFO:root:Training epoch 2, Iteration 240, Loss: 4.07961
INFO:root:Training epoch 2, Iteration 270, Loss: 4.07099
INFO:root:Training epoch 2, Iteration 300, Loss: 4.06173
INFO:root:Training epoch 2, Iteration 330, Loss: 4.03748
INFO:root:Training epoch 2, Iteration 360, Loss: 4.11765
INFO:root:Training epoch 2, Iteration 390, Loss: 4.10994
INFO:root:Training epoch 2, Iteration 420, Loss: 4.03873
INFO:root:Training epoch 2, Iteration 450, Loss: 4.14361
INFO:root:Training epoch 2, Iteration 480, Loss: 4.02332
INFO:root:Training epoch 2, Iteration 510, Loss: 4.14489
INFO:root:Training epoch 2, Iteration 540, Loss: 4.08492
INFO:root:Training epoch 2, Iteration 570, Loss: 4.07210
INFO:root:Training epoch 2, Iteration 600, Loss: 4.08219
INFO:root:Training epoch 2, Iteration 630, Loss: 4.05299
INFO:root:Training epoch 2, Iteration 660, Loss: 4.05051
INFO:root:Training epoch 2, Iteration 690, Loss: 4.00898
INFO:root:Training epoch 2, Iteration 720, Loss: 3.94496
INFO:root:Training epoch 2, Iteration 750, Loss: 4.17030
INFO:root:Training epoch 2, Iteration 780, Loss: 3.94919
INFO:root:Validation iteration 1, Loss: 3.48089
INFO:root:Validation iteration 10, Loss: 3.97755
INFO:root:Validation iteration 20, Loss: 3.82334
INFO:root:Validation iteration 30, Loss: 4.04345
INFO:root:Validation iteration 40, Loss: 3.87697
INFO:root:Validation iteration 50, Loss: 4.08507
INFO:root:Validation iteration 60, Loss: 4.05215
INFO:root:Validation iteration 70, Loss: 4.32510
INFO:root:Validation iteration 80, Loss: 3.97337
INFO:root:Validation iteration 90, Loss: 4.15061
INFO:root:Validation iteration 100, Loss: 4.24096
INFO:root:Validation iteration 110, Loss: 4.06102
INFO:root:Validation iteration 120, Loss: 4.04983
INFO:root:Validation iteration 130, Loss: 4.12355
INFO:root:Validation iteration 140, Loss: 4.09214
INFO:root:Validation iteration 150, Loss: 4.44200
INFO:root:Validation iteration 160, Loss: 4.00025
INFO:root:Validation iteration 170, Loss: 4.37055
INFO:root:Validation iteration 180, Loss: 4.04339
INFO:root:Validation iteration 190, Loss: 3.97662
INFO:root:Validation iteration 200, Loss: 3.86642
INFO:root:Validation iteration 210, Loss: 4.18424
INFO:root:Validation iteration 220, Loss: 4.26051
INFO:root:Validation iteration 230, Loss: 4.29025
INFO:root:Validation iteration 240, Loss: 4.25146
INFO:root:Validation iteration 250, Loss: 4.17531
INFO:root:Validation iteration 260, Loss: 4.15648
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.087
INFO:root:Validation accuracy: 0.054, Validation loss: 4.11199
INFO:root:Best validation accuracy: 0.054 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.73778
INFO:root:Validation iteration 10, Loss: 3.84042
INFO:root:Validation iteration 20, Loss: 3.98024
INFO:root:Validation iteration 30, Loss: 4.06668
INFO:root:Validation iteration 40, Loss: 4.21691
INFO:root:Validation iteration 50, Loss: 4.21865
INFO:root:Validation iteration 60, Loss: 4.13509
INFO:root:Validation iteration 70, Loss: 4.17411
INFO:root:Validation iteration 80, Loss: 4.46049
INFO:root:Validation iteration 90, Loss: 4.00043
INFO:root:Validation iteration 100, Loss: 4.26229
INFO:root:Validation iteration 110, Loss: 4.10470
INFO:root:Validation iteration 120, Loss: 4.09802
INFO:root:Validation iteration 130, Loss: 3.77722
INFO:root:Validation iteration 140, Loss: 4.36394
INFO:root:Validation iteration 150, Loss: 4.02474
INFO:root:Validation iteration 160, Loss: 3.93110
INFO:root:Validation iteration 170, Loss: 4.08405
INFO:root:Validation iteration 180, Loss: 4.10797
INFO:root:Validation iteration 190, Loss: 4.13050
INFO:root:Validation iteration 200, Loss: 4.13647
INFO:root:Validation iteration 210, Loss: 4.10760
INFO:root:Validation iteration 220, Loss: 4.17686
INFO:root:Validation iteration 230, Loss: 4.16755
INFO:root:Validation iteration 240, Loss: 4.12873
INFO:root:Validation iteration 250, Loss: 3.83249
INFO:root:Validation iteration 260, Loss: 4.18984
Test accuracy: 0.052, Test loss: 4.10004
INFO:root:Saving results...
INFO:root:Done!
"""

string7 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0003, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4758678078651428, 0.42080211639404297, 0.3604283332824707], 'std': [0.2790554165840149, 0.2741965651512146, 0.2640019357204437], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4758678078651428, 0.42080211639404297, 0.3604283332824707], std=[0.2790554165840149, 0.2741965651512146, 0.2640019357204437])']}}}
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 133MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.13124
INFO:root:Training epoch 1, Iteration 30, Loss: 5.20408
INFO:root:Training epoch 1, Iteration 60, Loss: 5.03323
INFO:root:Training epoch 1, Iteration 90, Loss: 4.87185
INFO:root:Training epoch 1, Iteration 120, Loss: 4.78487
INFO:root:Training epoch 1, Iteration 150, Loss: 4.64305
INFO:root:Training epoch 1, Iteration 180, Loss: 4.71091
INFO:root:Training epoch 1, Iteration 210, Loss: 4.70743
INFO:root:Training epoch 1, Iteration 240, Loss: 4.65436
INFO:root:Training epoch 1, Iteration 270, Loss: 4.59504
INFO:root:Training epoch 1, Iteration 300, Loss: 4.60071
INFO:root:Training epoch 1, Iteration 330, Loss: 4.58171
INFO:root:Training epoch 1, Iteration 360, Loss: 4.49397
INFO:root:Training epoch 1, Iteration 390, Loss: 4.38741
INFO:root:Training epoch 1, Iteration 420, Loss: 4.55022
INFO:root:Training epoch 1, Iteration 450, Loss: 4.38151
INFO:root:Training epoch 1, Iteration 480, Loss: 4.51827
INFO:root:Training epoch 1, Iteration 510, Loss: 4.46422
INFO:root:Training epoch 1, Iteration 540, Loss: 4.38294
INFO:root:Training epoch 1, Iteration 570, Loss: 4.38159
INFO:root:Training epoch 1, Iteration 600, Loss: 4.28987
INFO:root:Training epoch 1, Iteration 630, Loss: 4.31238
INFO:root:Training epoch 1, Iteration 660, Loss: 4.35108
INFO:root:Training epoch 1, Iteration 690, Loss: 4.33683
INFO:root:Training epoch 1, Iteration 720, Loss: 4.35552
INFO:root:Training epoch 1, Iteration 750, Loss: 4.26144
INFO:root:Training epoch 1, Iteration 780, Loss: 4.35935
INFO:root:Validation iteration 1, Loss: 3.28961
INFO:root:Validation iteration 10, Loss: 4.21422
INFO:root:Validation iteration 20, Loss: 4.08086
INFO:root:Validation iteration 30, Loss: 4.38759
INFO:root:Validation iteration 40, Loss: 4.26102
INFO:root:Validation iteration 50, Loss: 4.33366
INFO:root:Validation iteration 60, Loss: 4.25752
INFO:root:Validation iteration 70, Loss: 4.58350
INFO:root:Validation iteration 80, Loss: 4.30018
INFO:root:Validation iteration 90, Loss: 4.48931
INFO:root:Validation iteration 100, Loss: 4.39551
INFO:root:Validation iteration 110, Loss: 4.38223
INFO:root:Validation iteration 120, Loss: 4.17096
INFO:root:Validation iteration 130, Loss: 4.31704
INFO:root:Validation iteration 140, Loss: 4.47110
INFO:root:Validation iteration 150, Loss: 4.80344
INFO:root:Validation iteration 160, Loss: 4.33534
INFO:root:Validation iteration 170, Loss: 4.33105
INFO:root:Validation iteration 180, Loss: 4.64558
INFO:root:Validation iteration 190, Loss: 4.31072
INFO:root:Validation iteration 200, Loss: 4.33794
INFO:root:Validation iteration 210, Loss: 4.56515
INFO:root:Validation iteration 220, Loss: 4.42859
INFO:root:Validation iteration 230, Loss: 4.54873
INFO:root:Validation iteration 240, Loss: 4.53158
INFO:root:Validation iteration 250, Loss: 4.44373
INFO:root:Validation iteration 260, Loss: 4.45598
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.541
INFO:root:Validation accuracy: 0.029, Validation loss: 4.39655
INFO:root:Training epoch 2, Iteration 1, Loss: 4.76408
INFO:root:Training epoch 2, Iteration 30, Loss: 4.21623
INFO:root:Training epoch 2, Iteration 60, Loss: 4.17533
INFO:root:Training epoch 2, Iteration 90, Loss: 4.21184
INFO:root:Training epoch 2, Iteration 120, Loss: 4.15466
INFO:root:Training epoch 2, Iteration 150, Loss: 4.12251
INFO:root:Training epoch 2, Iteration 180, Loss: 4.28128
INFO:root:Training epoch 2, Iteration 210, Loss: 4.17833
INFO:root:Training epoch 2, Iteration 240, Loss: 4.31543
INFO:root:Training epoch 2, Iteration 270, Loss: 4.22413
INFO:root:Training epoch 2, Iteration 300, Loss: 4.26316
INFO:root:Training epoch 2, Iteration 330, Loss: 4.16755
INFO:root:Training epoch 2, Iteration 360, Loss: 4.18669
INFO:root:Training epoch 2, Iteration 390, Loss: 4.04159
INFO:root:Training epoch 2, Iteration 420, Loss: 4.15122
INFO:root:Training epoch 2, Iteration 450, Loss: 4.11371
INFO:root:Training epoch 2, Iteration 480, Loss: 4.14792
INFO:root:Training epoch 2, Iteration 510, Loss: 4.07723
INFO:root:Training epoch 2, Iteration 540, Loss: 4.19689
INFO:root:Training epoch 2, Iteration 570, Loss: 4.07142
INFO:root:Training epoch 2, Iteration 600, Loss: 4.22217
INFO:root:Training epoch 2, Iteration 630, Loss: 4.08461
INFO:root:Training epoch 2, Iteration 660, Loss: 4.22094
INFO:root:Training epoch 2, Iteration 690, Loss: 4.09510
INFO:root:Training epoch 2, Iteration 720, Loss: 4.00601
INFO:root:Training epoch 2, Iteration 750, Loss: 3.97393
INFO:root:Training epoch 2, Iteration 780, Loss: 4.08630
INFO:root:Validation iteration 1, Loss: 3.20511
INFO:root:Validation iteration 10, Loss: 3.98980
INFO:root:Validation iteration 20, Loss: 3.85922
INFO:root:Validation iteration 30, Loss: 4.08377
INFO:root:Validation iteration 40, Loss: 3.84693
INFO:root:Validation iteration 50, Loss: 3.99946
INFO:root:Validation iteration 60, Loss: 4.01230
INFO:root:Validation iteration 70, Loss: 4.23188
INFO:root:Validation iteration 80, Loss: 4.00346
INFO:root:Validation iteration 90, Loss: 3.97013
INFO:root:Validation iteration 100, Loss: 4.34673
INFO:root:Validation iteration 110, Loss: 3.93105
INFO:root:Validation iteration 120, Loss: 3.83243
INFO:root:Validation iteration 130, Loss: 4.01514
INFO:root:Validation iteration 140, Loss: 4.00530
INFO:root:Validation iteration 150, Loss: 4.36405
INFO:root:Validation iteration 160, Loss: 4.05882
INFO:root:Validation iteration 170, Loss: 4.18531
INFO:root:Validation iteration 180, Loss: 4.21478
INFO:root:Validation iteration 190, Loss: 3.90231
INFO:root:Validation iteration 200, Loss: 3.87589
INFO:root:Validation iteration 210, Loss: 4.09487
INFO:root:Validation iteration 220, Loss: 4.15333
INFO:root:Validation iteration 230, Loss: 4.23072
INFO:root:Validation iteration 240, Loss: 4.23459
INFO:root:Validation iteration 250, Loss: 4.21224
INFO:root:Validation iteration 260, Loss: 4.16124
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.149
INFO:root:Validation accuracy: 0.049, Validation loss: 4.06711
INFO:root:Best validation accuracy: 0.049 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.99486
INFO:root:Validation iteration 10, Loss: 3.84865
INFO:root:Validation iteration 20, Loss: 3.90621
INFO:root:Validation iteration 30, Loss: 4.01360
INFO:root:Validation iteration 40, Loss: 3.99572
INFO:root:Validation iteration 50, Loss: 4.30767
INFO:root:Validation iteration 60, Loss: 3.95406
INFO:root:Validation iteration 70, Loss: 4.00118
INFO:root:Validation iteration 80, Loss: 4.29134
INFO:root:Validation iteration 90, Loss: 4.05933
INFO:root:Validation iteration 100, Loss: 4.04906
INFO:root:Validation iteration 110, Loss: 4.01374
INFO:root:Validation iteration 120, Loss: 3.96459
INFO:root:Validation iteration 130, Loss: 3.77847
INFO:root:Validation iteration 140, Loss: 4.07367
INFO:root:Validation iteration 150, Loss: 4.10819
INFO:root:Validation iteration 160, Loss: 3.93608
INFO:root:Validation iteration 170, Loss: 3.89540
INFO:root:Validation iteration 180, Loss: 4.06821
INFO:root:Validation iteration 190, Loss: 4.08014
INFO:root:Validation iteration 200, Loss: 4.14615
INFO:root:Validation iteration 210, Loss: 4.09352
INFO:root:Validation iteration 220, Loss: 4.03349
INFO:root:Validation iteration 230, Loss: 4.02568
INFO:root:Validation iteration 240, Loss: 3.99992
INFO:root:Validation iteration 250, Loss: 4.02598
INFO:root:Validation iteration 260, Loss: 3.94485
Test accuracy: 0.047, Test loss: 4.01750
INFO:root:Saving results...
INFO:root:Done!
"""

string8 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0003, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=True, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4758678078651428, 0.42080211639404297, 0.3604283332824707], 'std': [0.2790554165840149, 0.2741965651512146, 0.2640019357204437], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4758678078651428, 0.42080211639404297, 0.3604283332824707], std=[0.2790554165840149, 0.2741965651512146, 0.2640019357204437])']}}}
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 88.4MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.19810
INFO:root:Training epoch 1, Iteration 30, Loss: 5.14361
INFO:root:Training epoch 1, Iteration 60, Loss: 4.97530
INFO:root:Training epoch 1, Iteration 90, Loss: 4.84386
INFO:root:Training epoch 1, Iteration 120, Loss: 4.72488
INFO:root:Training epoch 1, Iteration 150, Loss: 4.81432
INFO:root:Training epoch 1, Iteration 180, Loss: 4.65255
INFO:root:Training epoch 1, Iteration 210, Loss: 4.61549
INFO:root:Training epoch 1, Iteration 240, Loss: 4.70772
INFO:root:Training epoch 1, Iteration 270, Loss: 4.62823
INFO:root:Training epoch 1, Iteration 300, Loss: 4.68585
INFO:root:Training epoch 1, Iteration 330, Loss: 4.52726
INFO:root:Training epoch 1, Iteration 360, Loss: 4.59159
INFO:root:Training epoch 1, Iteration 390, Loss: 4.49597
INFO:root:Training epoch 1, Iteration 420, Loss: 4.55824
INFO:root:Training epoch 1, Iteration 450, Loss: 4.44758
INFO:root:Training epoch 1, Iteration 480, Loss: 4.44235
INFO:root:Training epoch 1, Iteration 510, Loss: 4.46091
INFO:root:Training epoch 1, Iteration 540, Loss: 4.47654
INFO:root:Training epoch 1, Iteration 570, Loss: 4.33631
INFO:root:Training epoch 1, Iteration 600, Loss: 4.33090
INFO:root:Training epoch 1, Iteration 630, Loss: 4.39861
INFO:root:Training epoch 1, Iteration 660, Loss: 4.31882
INFO:root:Training epoch 1, Iteration 690, Loss: 4.34852
INFO:root:Training epoch 1, Iteration 720, Loss: 4.40826
INFO:root:Training epoch 1, Iteration 750, Loss: 4.35531
INFO:root:Training epoch 1, Iteration 780, Loss: 4.25144
INFO:root:Validation iteration 1, Loss: 3.63475
INFO:root:Validation iteration 10, Loss: 4.07369
INFO:root:Validation iteration 20, Loss: 4.08439
INFO:root:Validation iteration 30, Loss: 4.13986
INFO:root:Validation iteration 40, Loss: 4.01237
INFO:root:Validation iteration 50, Loss: 4.20687
INFO:root:Validation iteration 60, Loss: 4.09536
INFO:root:Validation iteration 70, Loss: 4.36086
INFO:root:Validation iteration 80, Loss: 4.15227
INFO:root:Validation iteration 90, Loss: 4.28836
INFO:root:Validation iteration 100, Loss: 4.31414
INFO:root:Validation iteration 110, Loss: 4.19424
INFO:root:Validation iteration 120, Loss: 4.07335
INFO:root:Validation iteration 130, Loss: 4.22512
INFO:root:Validation iteration 140, Loss: 4.14644
INFO:root:Validation iteration 150, Loss: 4.56154
INFO:root:Validation iteration 160, Loss: 4.16961
INFO:root:Validation iteration 170, Loss: 4.23346
INFO:root:Validation iteration 180, Loss: 4.28024
INFO:root:Validation iteration 190, Loss: 4.07604
INFO:root:Validation iteration 200, Loss: 4.14950
INFO:root:Validation iteration 210, Loss: 4.29877
INFO:root:Validation iteration 220, Loss: 4.18847
INFO:root:Validation iteration 230, Loss: 4.41442
INFO:root:Validation iteration 240, Loss: 4.34458
INFO:root:Validation iteration 250, Loss: 4.26364
INFO:root:Validation iteration 260, Loss: 4.32771
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.552
INFO:root:Validation accuracy: 0.036, Validation loss: 4.21746
INFO:root:Training epoch 2, Iteration 1, Loss: 4.71873
INFO:root:Training epoch 2, Iteration 30, Loss: 4.30758
INFO:root:Training epoch 2, Iteration 60, Loss: 4.23143
INFO:root:Training epoch 2, Iteration 90, Loss: 4.14817
INFO:root:Training epoch 2, Iteration 120, Loss: 4.04882
INFO:root:Training epoch 2, Iteration 150, Loss: 4.28877
INFO:root:Training epoch 2, Iteration 180, Loss: 4.26556
INFO:root:Training epoch 2, Iteration 210, Loss: 4.24691
INFO:root:Training epoch 2, Iteration 240, Loss: 4.24988
INFO:root:Training epoch 2, Iteration 270, Loss: 4.25701
INFO:root:Training epoch 2, Iteration 300, Loss: 4.11009
INFO:root:Training epoch 2, Iteration 330, Loss: 4.17775
INFO:root:Training epoch 2, Iteration 360, Loss: 4.17060
INFO:root:Training epoch 2, Iteration 390, Loss: 4.19381
INFO:root:Training epoch 2, Iteration 420, Loss: 4.08660
INFO:root:Training epoch 2, Iteration 450, Loss: 4.13793
INFO:root:Training epoch 2, Iteration 480, Loss: 4.15181
INFO:root:Training epoch 2, Iteration 510, Loss: 4.13232
INFO:root:Training epoch 2, Iteration 540, Loss: 4.09740
INFO:root:Training epoch 2, Iteration 570, Loss: 3.93247
INFO:root:Training epoch 2, Iteration 600, Loss: 4.07094
INFO:root:Training epoch 2, Iteration 630, Loss: 4.16548
INFO:root:Training epoch 2, Iteration 660, Loss: 4.10638
INFO:root:Training epoch 2, Iteration 690, Loss: 4.05983
INFO:root:Training epoch 2, Iteration 720, Loss: 4.09814
INFO:root:Training epoch 2, Iteration 750, Loss: 4.02417
INFO:root:Training epoch 2, Iteration 780, Loss: 4.12825
INFO:root:Validation iteration 1, Loss: 3.31246
INFO:root:Validation iteration 10, Loss: 3.98298
INFO:root:Validation iteration 20, Loss: 3.99236
INFO:root:Validation iteration 30, Loss: 4.02905
INFO:root:Validation iteration 40, Loss: 3.90793
INFO:root:Validation iteration 50, Loss: 4.09610
INFO:root:Validation iteration 60, Loss: 3.95753
INFO:root:Validation iteration 70, Loss: 4.23525
INFO:root:Validation iteration 80, Loss: 4.10662
INFO:root:Validation iteration 90, Loss: 4.12732
INFO:root:Validation iteration 100, Loss: 4.25582
INFO:root:Validation iteration 110, Loss: 4.07325
INFO:root:Validation iteration 120, Loss: 3.87587
INFO:root:Validation iteration 130, Loss: 4.08006
INFO:root:Validation iteration 140, Loss: 4.00238
INFO:root:Validation iteration 150, Loss: 4.32115
INFO:root:Validation iteration 160, Loss: 4.13144
INFO:root:Validation iteration 170, Loss: 4.11330
INFO:root:Validation iteration 180, Loss: 4.32265
INFO:root:Validation iteration 190, Loss: 3.86807
INFO:root:Validation iteration 200, Loss: 3.98762
INFO:root:Validation iteration 210, Loss: 4.05999
INFO:root:Validation iteration 220, Loss: 4.03166
INFO:root:Validation iteration 230, Loss: 4.15835
INFO:root:Validation iteration 240, Loss: 4.26209
INFO:root:Validation iteration 250, Loss: 4.01155
INFO:root:Validation iteration 260, Loss: 4.20515
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.149
INFO:root:Validation accuracy: 0.058, Validation loss: 4.08742
INFO:root:Best validation accuracy: 0.058 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 4.20238
INFO:root:Validation iteration 10, Loss: 3.97305
INFO:root:Validation iteration 20, Loss: 3.94411
INFO:root:Validation iteration 30, Loss: 4.09380
INFO:root:Validation iteration 40, Loss: 4.10739
INFO:root:Validation iteration 50, Loss: 4.10686
INFO:root:Validation iteration 60, Loss: 4.03883
INFO:root:Validation iteration 70, Loss: 3.99166
INFO:root:Validation iteration 80, Loss: 4.19354
INFO:root:Validation iteration 90, Loss: 3.97801
INFO:root:Validation iteration 100, Loss: 4.10118
INFO:root:Validation iteration 110, Loss: 4.02872
INFO:root:Validation iteration 120, Loss: 3.93114
INFO:root:Validation iteration 130, Loss: 3.83269
INFO:root:Validation iteration 140, Loss: 4.10232
INFO:root:Validation iteration 150, Loss: 4.06640
INFO:root:Validation iteration 160, Loss: 3.80459
INFO:root:Validation iteration 170, Loss: 3.99885
INFO:root:Validation iteration 180, Loss: 4.10849
INFO:root:Validation iteration 190, Loss: 4.09566
INFO:root:Validation iteration 200, Loss: 4.17331
INFO:root:Validation iteration 210, Loss: 4.11431
INFO:root:Validation iteration 220, Loss: 4.15253
INFO:root:Validation iteration 230, Loss: 4.18076
INFO:root:Validation iteration 240, Loss: 4.11183
INFO:root:Validation iteration 250, Loss: 3.84673
INFO:root:Validation iteration 260, Loss: 4.02518
Test accuracy: 0.054, Test loss: 4.03952
INFO:root:Saving results...
INFO:root:Done!
"""

string9 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4758678078651428, 0.42080211639404297, 0.3604283332824707], 'std': [0.2790554165840149, 0.2741965651512146, 0.2640019357204437], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4758678078651428, 0.42080211639404297, 0.3604283332824707], std=[0.2790554165840149, 0.2741965651512146, 0.2640019357204437])']}}}
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 185MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.21745
INFO:root:Training epoch 1, Iteration 30, Loss: 5.03924
INFO:root:Training epoch 1, Iteration 60, Loss: 4.99209
INFO:root:Training epoch 1, Iteration 90, Loss: 4.93721
INFO:root:Training epoch 1, Iteration 120, Loss: 4.75406
INFO:root:Training epoch 1, Iteration 150, Loss: 4.75985
INFO:root:Training epoch 1, Iteration 180, Loss: 4.67522
INFO:root:Training epoch 1, Iteration 210, Loss: 4.69336
INFO:root:Training epoch 1, Iteration 240, Loss: 4.55729
INFO:root:Training epoch 1, Iteration 270, Loss: 4.54813
INFO:root:Training epoch 1, Iteration 300, Loss: 4.59706
INFO:root:Training epoch 1, Iteration 330, Loss: 4.52822
INFO:root:Training epoch 1, Iteration 360, Loss: 4.47013
INFO:root:Training epoch 1, Iteration 390, Loss: 4.49118
INFO:root:Training epoch 1, Iteration 420, Loss: 4.39119
INFO:root:Training epoch 1, Iteration 450, Loss: 4.29667
INFO:root:Training epoch 1, Iteration 480, Loss: 4.37030
INFO:root:Training epoch 1, Iteration 510, Loss: 4.38296
INFO:root:Training epoch 1, Iteration 540, Loss: 4.37397
INFO:root:Training epoch 1, Iteration 570, Loss: 4.32092
INFO:root:Training epoch 1, Iteration 600, Loss: 4.33492
INFO:root:Training epoch 1, Iteration 630, Loss: 4.30134
INFO:root:Training epoch 1, Iteration 660, Loss: 4.34901
INFO:root:Training epoch 1, Iteration 690, Loss: 4.36576
INFO:root:Training epoch 1, Iteration 720, Loss: 4.26680
INFO:root:Training epoch 1, Iteration 750, Loss: 4.15383
INFO:root:Training epoch 1, Iteration 780, Loss: 4.29059
INFO:root:Validation iteration 1, Loss: 3.51385
INFO:root:Validation iteration 10, Loss: 4.21464
INFO:root:Validation iteration 20, Loss: 4.02106
INFO:root:Validation iteration 30, Loss: 4.39809
INFO:root:Validation iteration 40, Loss: 4.19018
INFO:root:Validation iteration 50, Loss: 4.27020
INFO:root:Validation iteration 60, Loss: 4.21224
INFO:root:Validation iteration 70, Loss: 4.48809
INFO:root:Validation iteration 80, Loss: 4.14540
INFO:root:Validation iteration 90, Loss: 4.23735
INFO:root:Validation iteration 100, Loss: 4.43713
INFO:root:Validation iteration 110, Loss: 4.17944
INFO:root:Validation iteration 120, Loss: 4.10358
INFO:root:Validation iteration 130, Loss: 4.43390
INFO:root:Validation iteration 140, Loss: 4.35158
INFO:root:Validation iteration 150, Loss: 4.60685
INFO:root:Validation iteration 160, Loss: 4.26481
INFO:root:Validation iteration 170, Loss: 4.34444
INFO:root:Validation iteration 180, Loss: 4.44571
INFO:root:Validation iteration 190, Loss: 4.09529
INFO:root:Validation iteration 200, Loss: 4.33288
INFO:root:Validation iteration 210, Loss: 4.44555
INFO:root:Validation iteration 220, Loss: 4.29072
INFO:root:Validation iteration 230, Loss: 4.37964
INFO:root:Validation iteration 240, Loss: 4.43686
INFO:root:Validation iteration 250, Loss: 4.42966
INFO:root:Validation iteration 260, Loss: 4.52328
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.507
INFO:root:Validation accuracy: 0.066, Validation loss: 4.31760
INFO:root:Training epoch 2, Iteration 1, Loss: 4.56363
INFO:root:Training epoch 2, Iteration 30, Loss: 4.25574
INFO:root:Training epoch 2, Iteration 60, Loss: 4.13214
INFO:root:Training epoch 2, Iteration 90, Loss: 4.25251
INFO:root:Training epoch 2, Iteration 120, Loss: 4.03910
INFO:root:Training epoch 2, Iteration 150, Loss: 4.16888
INFO:root:Training epoch 2, Iteration 180, Loss: 4.14825
INFO:root:Training epoch 2, Iteration 210, Loss: 4.11841
INFO:root:Training epoch 2, Iteration 240, Loss: 4.23143
INFO:root:Training epoch 2, Iteration 270, Loss: 4.08968
INFO:root:Training epoch 2, Iteration 300, Loss: 4.14139
INFO:root:Training epoch 2, Iteration 330, Loss: 3.93219
INFO:root:Training epoch 2, Iteration 360, Loss: 4.16766
INFO:root:Training epoch 2, Iteration 390, Loss: 4.07256
INFO:root:Training epoch 2, Iteration 420, Loss: 4.11553
INFO:root:Training epoch 2, Iteration 450, Loss: 4.06959
INFO:root:Training epoch 2, Iteration 480, Loss: 3.97345
INFO:root:Training epoch 2, Iteration 510, Loss: 4.09512
INFO:root:Training epoch 2, Iteration 540, Loss: 4.07558
INFO:root:Training epoch 2, Iteration 570, Loss: 4.13387
INFO:root:Training epoch 2, Iteration 600, Loss: 4.07919
INFO:root:Training epoch 2, Iteration 630, Loss: 4.02198
INFO:root:Training epoch 2, Iteration 660, Loss: 4.06363
INFO:root:Training epoch 2, Iteration 690, Loss: 3.94209
INFO:root:Training epoch 2, Iteration 720, Loss: 4.02208
INFO:root:Training epoch 2, Iteration 750, Loss: 3.97433
INFO:root:Training epoch 2, Iteration 780, Loss: 3.96360
INFO:root:Validation iteration 1, Loss: 2.70194
INFO:root:Validation iteration 10, Loss: 3.70895
INFO:root:Validation iteration 20, Loss: 3.77575
INFO:root:Validation iteration 30, Loss: 3.95194
INFO:root:Validation iteration 40, Loss: 3.93773
INFO:root:Validation iteration 50, Loss: 3.96118
INFO:root:Validation iteration 60, Loss: 3.87845
INFO:root:Validation iteration 70, Loss: 4.25866
INFO:root:Validation iteration 80, Loss: 4.05103
INFO:root:Validation iteration 90, Loss: 3.91398
INFO:root:Validation iteration 100, Loss: 4.32215
INFO:root:Validation iteration 110, Loss: 3.96939
INFO:root:Validation iteration 120, Loss: 3.83920
INFO:root:Validation iteration 130, Loss: 3.96299
INFO:root:Validation iteration 140, Loss: 3.95263
INFO:root:Validation iteration 150, Loss: 4.29895
INFO:root:Validation iteration 160, Loss: 4.01472
INFO:root:Validation iteration 170, Loss: 4.08911
INFO:root:Validation iteration 180, Loss: 4.11119
INFO:root:Validation iteration 190, Loss: 3.83771
INFO:root:Validation iteration 200, Loss: 3.77690
INFO:root:Validation iteration 210, Loss: 3.96446
INFO:root:Validation iteration 220, Loss: 4.04742
INFO:root:Validation iteration 230, Loss: 4.18467
INFO:root:Validation iteration 240, Loss: 4.18831
INFO:root:Validation iteration 250, Loss: 3.95906
INFO:root:Validation iteration 260, Loss: 4.12958
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.085
INFO:root:Validation accuracy: 0.100, Validation loss: 4.00828
INFO:root:Best validation accuracy: 0.100 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.75662
INFO:root:Validation iteration 10, Loss: 3.84728
INFO:root:Validation iteration 20, Loss: 3.95167
INFO:root:Validation iteration 30, Loss: 3.99295
INFO:root:Validation iteration 40, Loss: 4.06411
INFO:root:Validation iteration 50, Loss: 4.05529
INFO:root:Validation iteration 60, Loss: 3.90136
INFO:root:Validation iteration 70, Loss: 3.84789
INFO:root:Validation iteration 80, Loss: 4.11477
INFO:root:Validation iteration 90, Loss: 3.91300
INFO:root:Validation iteration 100, Loss: 4.15774
INFO:root:Validation iteration 110, Loss: 4.00063
INFO:root:Validation iteration 120, Loss: 4.07767
INFO:root:Validation iteration 130, Loss: 3.85425
INFO:root:Validation iteration 140, Loss: 4.08927
INFO:root:Validation iteration 150, Loss: 4.05189
INFO:root:Validation iteration 160, Loss: 3.78188
INFO:root:Validation iteration 170, Loss: 3.95751
INFO:root:Validation iteration 180, Loss: 3.98495
INFO:root:Validation iteration 190, Loss: 4.07429
INFO:root:Validation iteration 200, Loss: 4.04422
INFO:root:Validation iteration 210, Loss: 4.07875
INFO:root:Validation iteration 220, Loss: 4.14350
INFO:root:Validation iteration 230, Loss: 3.94817
INFO:root:Validation iteration 240, Loss: 4.17538
INFO:root:Validation iteration 250, Loss: 3.86917
INFO:root:Validation iteration 260, Loss: 3.92188
Test accuracy: 0.145, Test loss: 3.99764
INFO:root:Saving results...
INFO:root:Done!
"""

string10="""
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=32, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/398
INFO:root:Processing batch 2/398
INFO:root:Processing batch 3/398
INFO:root:Processing batch 4/398
INFO:root:Processing batch 5/398
INFO:root:Processing batch 6/398
INFO:root:Processing batch 7/398
INFO:root:Processing batch 8/398
INFO:root:Processing batch 9/398
INFO:root:Processing batch 10/398
INFO:root:Processing batch 11/398
INFO:root:Processing batch 12/398
INFO:root:Processing batch 13/398
INFO:root:Processing batch 14/398
INFO:root:Processing batch 15/398
INFO:root:Processing batch 16/398
INFO:root:Processing batch 17/398
INFO:root:Processing batch 18/398
INFO:root:Processing batch 19/398
INFO:root:Processing batch 20/398
INFO:root:Processing batch 21/398
INFO:root:Processing batch 22/398
INFO:root:Processing batch 23/398
INFO:root:Processing batch 24/398
INFO:root:Processing batch 25/398
INFO:root:Processing batch 26/398
INFO:root:Processing batch 27/398
INFO:root:Processing batch 28/398
INFO:root:Processing batch 29/398
INFO:root:Processing batch 30/398
INFO:root:Processing batch 31/398
INFO:root:Processing batch 32/398
INFO:root:Processing batch 33/398
INFO:root:Processing batch 34/398
INFO:root:Processing batch 35/398
INFO:root:Processing batch 36/398
INFO:root:Processing batch 37/398
INFO:root:Processing batch 38/398
INFO:root:Processing batch 39/398
INFO:root:Processing batch 40/398
INFO:root:Processing batch 41/398
INFO:root:Processing batch 42/398
INFO:root:Processing batch 43/398
INFO:root:Processing batch 44/398
INFO:root:Processing batch 45/398
INFO:root:Processing batch 46/398
INFO:root:Processing batch 47/398
INFO:root:Processing batch 48/398
INFO:root:Processing batch 49/398
INFO:root:Processing batch 50/398
INFO:root:Processing batch 51/398
INFO:root:Processing batch 52/398
INFO:root:Processing batch 53/398
INFO:root:Processing batch 54/398
INFO:root:Processing batch 55/398
INFO:root:Processing batch 56/398
INFO:root:Processing batch 57/398
INFO:root:Processing batch 58/398
INFO:root:Processing batch 59/398
INFO:root:Processing batch 60/398
INFO:root:Processing batch 61/398
INFO:root:Processing batch 62/398
INFO:root:Processing batch 63/398
INFO:root:Processing batch 64/398
INFO:root:Processing batch 65/398
INFO:root:Processing batch 66/398
INFO:root:Processing batch 67/398
INFO:root:Processing batch 68/398
INFO:root:Processing batch 69/398
INFO:root:Processing batch 70/398
INFO:root:Processing batch 71/398
INFO:root:Processing batch 72/398
INFO:root:Processing batch 73/398
INFO:root:Processing batch 74/398
INFO:root:Processing batch 75/398
INFO:root:Processing batch 76/398
INFO:root:Processing batch 77/398
INFO:root:Processing batch 78/398
INFO:root:Processing batch 79/398
INFO:root:Processing batch 80/398
INFO:root:Processing batch 81/398
INFO:root:Processing batch 82/398
INFO:root:Processing batch 83/398
INFO:root:Processing batch 84/398
INFO:root:Processing batch 85/398
INFO:root:Processing batch 86/398
INFO:root:Processing batch 87/398
INFO:root:Processing batch 88/398
INFO:root:Processing batch 89/398
INFO:root:Processing batch 90/398
INFO:root:Processing batch 91/398
INFO:root:Processing batch 92/398
INFO:root:Processing batch 93/398
INFO:root:Processing batch 94/398
INFO:root:Processing batch 95/398
INFO:root:Processing batch 96/398
INFO:root:Processing batch 97/398
INFO:root:Processing batch 98/398
INFO:root:Processing batch 99/398
INFO:root:Processing batch 100/398
INFO:root:Processing batch 101/398
INFO:root:Processing batch 102/398
INFO:root:Processing batch 103/398
INFO:root:Processing batch 104/398
INFO:root:Processing batch 105/398
INFO:root:Processing batch 106/398
INFO:root:Processing batch 107/398
INFO:root:Processing batch 108/398
INFO:root:Processing batch 109/398
INFO:root:Processing batch 110/398
INFO:root:Processing batch 111/398
INFO:root:Processing batch 112/398
INFO:root:Processing batch 113/398
INFO:root:Processing batch 114/398
INFO:root:Processing batch 115/398
INFO:root:Processing batch 116/398
INFO:root:Processing batch 117/398
INFO:root:Processing batch 118/398
INFO:root:Processing batch 119/398
INFO:root:Processing batch 120/398
INFO:root:Processing batch 121/398
INFO:root:Processing batch 122/398
INFO:root:Processing batch 123/398
INFO:root:Processing batch 124/398
INFO:root:Processing batch 125/398
INFO:root:Processing batch 126/398
INFO:root:Processing batch 127/398
INFO:root:Processing batch 128/398
INFO:root:Processing batch 129/398
INFO:root:Processing batch 130/398
INFO:root:Processing batch 131/398
INFO:root:Processing batch 132/398
INFO:root:Processing batch 133/398
INFO:root:Processing batch 134/398
INFO:root:Processing batch 135/398
INFO:root:Processing batch 136/398
INFO:root:Processing batch 137/398
INFO:root:Processing batch 138/398
INFO:root:Processing batch 139/398
INFO:root:Processing batch 140/398
INFO:root:Processing batch 141/398
INFO:root:Processing batch 142/398
INFO:root:Processing batch 143/398
INFO:root:Processing batch 144/398
INFO:root:Processing batch 145/398
INFO:root:Processing batch 146/398
INFO:root:Processing batch 147/398
INFO:root:Processing batch 148/398
INFO:root:Processing batch 149/398
INFO:root:Processing batch 150/398
INFO:root:Processing batch 151/398
INFO:root:Processing batch 152/398
INFO:root:Processing batch 153/398
INFO:root:Processing batch 154/398
INFO:root:Processing batch 155/398
INFO:root:Processing batch 156/398
INFO:root:Processing batch 157/398
INFO:root:Processing batch 158/398
INFO:root:Processing batch 159/398
INFO:root:Processing batch 160/398
INFO:root:Processing batch 161/398
INFO:root:Processing batch 162/398
INFO:root:Processing batch 163/398
INFO:root:Processing batch 164/398
INFO:root:Processing batch 165/398
INFO:root:Processing batch 166/398
INFO:root:Processing batch 167/398
INFO:root:Processing batch 168/398
INFO:root:Processing batch 169/398
INFO:root:Processing batch 170/398
INFO:root:Processing batch 171/398
INFO:root:Processing batch 172/398
INFO:root:Processing batch 173/398
INFO:root:Processing batch 174/398
INFO:root:Processing batch 175/398
INFO:root:Processing batch 176/398
INFO:root:Processing batch 177/398
INFO:root:Processing batch 178/398
INFO:root:Processing batch 179/398
INFO:root:Processing batch 180/398
INFO:root:Processing batch 181/398
INFO:root:Processing batch 182/398
INFO:root:Processing batch 183/398
INFO:root:Processing batch 184/398
INFO:root:Processing batch 185/398
INFO:root:Processing batch 186/398
INFO:root:Processing batch 187/398
INFO:root:Processing batch 188/398
INFO:root:Processing batch 189/398
INFO:root:Processing batch 190/398
INFO:root:Processing batch 191/398
INFO:root:Processing batch 192/398
INFO:root:Processing batch 193/398
INFO:root:Processing batch 194/398
INFO:root:Processing batch 195/398
INFO:root:Processing batch 196/398
INFO:root:Processing batch 197/398
INFO:root:Processing batch 198/398
INFO:root:Processing batch 199/398
INFO:root:Processing batch 200/398
INFO:root:Processing batch 201/398
INFO:root:Processing batch 202/398
INFO:root:Processing batch 203/398
INFO:root:Processing batch 204/398
INFO:root:Processing batch 205/398
INFO:root:Processing batch 206/398
INFO:root:Processing batch 207/398
INFO:root:Processing batch 208/398
INFO:root:Processing batch 209/398
INFO:root:Processing batch 210/398
INFO:root:Processing batch 211/398
INFO:root:Processing batch 212/398
INFO:root:Processing batch 213/398
INFO:root:Processing batch 214/398
INFO:root:Processing batch 215/398
INFO:root:Processing batch 216/398
INFO:root:Processing batch 217/398
INFO:root:Processing batch 218/398
INFO:root:Processing batch 219/398
INFO:root:Processing batch 220/398
INFO:root:Processing batch 221/398
INFO:root:Processing batch 222/398
INFO:root:Processing batch 223/398
INFO:root:Processing batch 224/398
INFO:root:Processing batch 225/398
INFO:root:Processing batch 226/398
INFO:root:Processing batch 227/398
INFO:root:Processing batch 228/398
INFO:root:Processing batch 229/398
INFO:root:Processing batch 230/398
INFO:root:Processing batch 231/398
INFO:root:Processing batch 232/398
INFO:root:Processing batch 233/398
INFO:root:Processing batch 234/398
INFO:root:Processing batch 235/398
INFO:root:Processing batch 236/398
INFO:root:Processing batch 237/398
INFO:root:Processing batch 238/398
INFO:root:Processing batch 239/398
INFO:root:Processing batch 240/398
INFO:root:Processing batch 241/398
INFO:root:Processing batch 242/398
INFO:root:Processing batch 243/398
INFO:root:Processing batch 244/398
INFO:root:Processing batch 245/398
INFO:root:Processing batch 246/398
INFO:root:Processing batch 247/398
INFO:root:Processing batch 248/398
INFO:root:Processing batch 249/398
INFO:root:Processing batch 250/398
INFO:root:Processing batch 251/398
INFO:root:Processing batch 252/398
INFO:root:Processing batch 253/398
INFO:root:Processing batch 254/398
INFO:root:Processing batch 255/398
INFO:root:Processing batch 256/398
INFO:root:Processing batch 257/398
INFO:root:Processing batch 258/398
INFO:root:Processing batch 259/398
INFO:root:Processing batch 260/398
INFO:root:Processing batch 261/398
INFO:root:Processing batch 262/398
INFO:root:Processing batch 263/398
INFO:root:Processing batch 264/398
INFO:root:Processing batch 265/398
INFO:root:Processing batch 266/398
INFO:root:Processing batch 267/398
INFO:root:Processing batch 268/398
INFO:root:Processing batch 269/398
INFO:root:Processing batch 270/398
INFO:root:Processing batch 271/398
INFO:root:Processing batch 272/398
INFO:root:Processing batch 273/398
INFO:root:Processing batch 274/398
INFO:root:Processing batch 275/398
INFO:root:Processing batch 276/398
INFO:root:Processing batch 277/398
INFO:root:Processing batch 278/398
INFO:root:Processing batch 279/398
INFO:root:Processing batch 280/398
INFO:root:Processing batch 281/398
INFO:root:Processing batch 282/398
INFO:root:Processing batch 283/398
INFO:root:Processing batch 284/398
INFO:root:Processing batch 285/398
INFO:root:Processing batch 286/398
INFO:root:Processing batch 287/398
INFO:root:Processing batch 288/398
INFO:root:Processing batch 289/398
INFO:root:Processing batch 290/398
INFO:root:Processing batch 291/398
INFO:root:Processing batch 292/398
INFO:root:Processing batch 293/398
INFO:root:Processing batch 294/398
INFO:root:Processing batch 295/398
INFO:root:Processing batch 296/398
INFO:root:Processing batch 297/398
INFO:root:Processing batch 298/398
INFO:root:Processing batch 299/398
INFO:root:Processing batch 300/398
INFO:root:Processing batch 301/398
INFO:root:Processing batch 302/398
INFO:root:Processing batch 303/398
INFO:root:Processing batch 304/398
INFO:root:Processing batch 305/398
INFO:root:Processing batch 306/398
INFO:root:Processing batch 307/398
INFO:root:Processing batch 308/398
INFO:root:Processing batch 309/398
INFO:root:Processing batch 310/398
INFO:root:Processing batch 311/398
INFO:root:Processing batch 312/398
INFO:root:Processing batch 313/398
INFO:root:Processing batch 314/398
INFO:root:Processing batch 315/398
INFO:root:Processing batch 316/398
INFO:root:Processing batch 317/398
INFO:root:Processing batch 318/398
INFO:root:Processing batch 319/398
INFO:root:Processing batch 320/398
INFO:root:Processing batch 321/398
INFO:root:Processing batch 322/398
INFO:root:Processing batch 323/398
INFO:root:Processing batch 324/398
INFO:root:Processing batch 325/398
INFO:root:Processing batch 326/398
INFO:root:Processing batch 327/398
INFO:root:Processing batch 328/398
INFO:root:Processing batch 329/398
INFO:root:Processing batch 330/398
INFO:root:Processing batch 331/398
INFO:root:Processing batch 332/398
INFO:root:Processing batch 333/398
INFO:root:Processing batch 334/398
INFO:root:Processing batch 335/398
INFO:root:Processing batch 336/398
INFO:root:Processing batch 337/398
INFO:root:Processing batch 338/398
INFO:root:Processing batch 339/398
INFO:root:Processing batch 340/398
INFO:root:Processing batch 341/398
INFO:root:Processing batch 342/398
INFO:root:Processing batch 343/398
INFO:root:Processing batch 344/398
INFO:root:Processing batch 345/398
INFO:root:Processing batch 346/398
INFO:root:Processing batch 347/398
INFO:root:Processing batch 348/398
INFO:root:Processing batch 349/398
INFO:root:Processing batch 350/398
INFO:root:Processing batch 351/398
INFO:root:Processing batch 352/398
INFO:root:Processing batch 353/398
INFO:root:Processing batch 354/398
INFO:root:Processing batch 355/398
INFO:root:Processing batch 356/398
INFO:root:Processing batch 357/398
INFO:root:Processing batch 358/398
INFO:root:Processing batch 359/398
INFO:root:Processing batch 360/398
INFO:root:Processing batch 361/398
INFO:root:Processing batch 362/398
INFO:root:Processing batch 363/398
INFO:root:Processing batch 364/398
INFO:root:Processing batch 365/398
INFO:root:Processing batch 366/398
INFO:root:Processing batch 367/398
INFO:root:Processing batch 368/398
INFO:root:Processing batch 369/398
INFO:root:Processing batch 370/398
INFO:root:Processing batch 371/398
INFO:root:Processing batch 372/398
INFO:root:Processing batch 373/398
INFO:root:Processing batch 374/398
INFO:root:Processing batch 375/398
INFO:root:Processing batch 376/398
INFO:root:Processing batch 377/398
INFO:root:Processing batch 378/398
INFO:root:Processing batch 379/398
INFO:root:Processing batch 380/398
INFO:root:Processing batch 381/398
INFO:root:Processing batch 382/398
INFO:root:Processing batch 383/398
INFO:root:Processing batch 384/398
INFO:root:Processing batch 385/398
INFO:root:Processing batch 386/398
INFO:root:Processing batch 387/398
INFO:root:Processing batch 388/398
INFO:root:Processing batch 389/398
INFO:root:Processing batch 390/398
INFO:root:Processing batch 391/398
INFO:root:Processing batch 392/398
INFO:root:Processing batch 393/398
INFO:root:Processing batch 394/398
INFO:root:Processing batch 395/398
INFO:root:Processing batch 396/398
INFO:root:Processing batch 397/398
INFO:root:Processing batch 398/398
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47586774826049805, 0.42080193758010864, 0.36042824387550354], 'std': [0.2790556848049164, 0.27419695258140564, 0.2640022039413452], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47586774826049805, 0.42080193758010864, 0.36042824387550354], std=[0.2790556848049164, 0.27419695258140564, 0.2640022039413452])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.10509
INFO:root:Training epoch 1, Iteration 30, Loss: 5.23612
INFO:root:Training epoch 1, Iteration 60, Loss: 4.97681
INFO:root:Training epoch 1, Iteration 90, Loss: 4.78189
INFO:root:Training epoch 1, Iteration 120, Loss: 4.74478
INFO:root:Training epoch 1, Iteration 150, Loss: 4.74685
INFO:root:Training epoch 1, Iteration 180, Loss: 4.64434
INFO:root:Training epoch 1, Iteration 210, Loss: 4.52694
INFO:root:Training epoch 1, Iteration 240, Loss: 4.66596
INFO:root:Training epoch 1, Iteration 270, Loss: 4.61401
INFO:root:Training epoch 1, Iteration 300, Loss: 4.60328
INFO:root:Training epoch 1, Iteration 330, Loss: 4.55946
INFO:root:Training epoch 1, Iteration 360, Loss: 4.53275
INFO:root:Training epoch 1, Iteration 390, Loss: 4.49183
INFO:root:Validation iteration 1, Loss: 4.15459
INFO:root:Validation iteration 10, Loss: 4.42738
INFO:root:Validation iteration 20, Loss: 4.39039
INFO:root:Validation iteration 30, Loss: 4.50644
INFO:root:Validation iteration 40, Loss: 4.58366
INFO:root:Validation iteration 50, Loss: 4.58663
INFO:root:Validation iteration 60, Loss: 4.49243
INFO:root:Validation iteration 70, Loss: 4.50157
INFO:root:Validation iteration 80, Loss: 4.67362
INFO:root:Validation iteration 90, Loss: 4.64751
INFO:root:Validation iteration 100, Loss: 4.44030
INFO:root:Validation iteration 110, Loss: 4.67947
INFO:root:Validation iteration 120, Loss: 4.70264
INFO:root:Validation iteration 130, Loss: 4.64692
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.697
INFO:root:Validation accuracy: 0.034, Validation loss: 4.56493
INFO:root:Training epoch 2, Iteration 1, Loss: 4.16887
INFO:root:Training epoch 2, Iteration 30, Loss: 4.41584
INFO:root:Training epoch 2, Iteration 60, Loss: 4.43005
INFO:root:Training epoch 2, Iteration 90, Loss: 4.48943
INFO:root:Training epoch 2, Iteration 120, Loss: 4.42797
INFO:root:Training epoch 2, Iteration 150, Loss: 4.42831
INFO:root:Training epoch 2, Iteration 180, Loss: 4.25810
INFO:root:Training epoch 2, Iteration 210, Loss: 4.42255
INFO:root:Training epoch 2, Iteration 240, Loss: 4.38014
INFO:root:Training epoch 2, Iteration 270, Loss: 4.28410
INFO:root:Training epoch 2, Iteration 300, Loss: 4.30366
INFO:root:Training epoch 2, Iteration 330, Loss: 4.30114
INFO:root:Training epoch 2, Iteration 360, Loss: 4.35039
INFO:root:Training epoch 2, Iteration 390, Loss: 4.27136
INFO:root:Validation iteration 1, Loss: 3.82907
INFO:root:Validation iteration 10, Loss: 4.18196
INFO:root:Validation iteration 20, Loss: 4.20392
INFO:root:Validation iteration 30, Loss: 4.25405
INFO:root:Validation iteration 40, Loss: 4.32639
INFO:root:Validation iteration 50, Loss: 4.38104
INFO:root:Validation iteration 60, Loss: 4.18317
INFO:root:Validation iteration 70, Loss: 4.27176
INFO:root:Validation iteration 80, Loss: 4.44138
INFO:root:Validation iteration 90, Loss: 4.34928
INFO:root:Validation iteration 100, Loss: 4.23714
INFO:root:Validation iteration 110, Loss: 4.38353
INFO:root:Validation iteration 120, Loss: 4.41948
INFO:root:Validation iteration 130, Loss: 4.31390
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.367
INFO:root:Validation accuracy: 0.051, Validation loss: 4.30287
INFO:root:Best validation accuracy: 0.051 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 4.27593
INFO:root:Validation iteration 10, Loss: 4.29360
INFO:root:Validation iteration 20, Loss: 4.28750
INFO:root:Validation iteration 30, Loss: 4.27344
INFO:root:Validation iteration 40, Loss: 4.29263
INFO:root:Validation iteration 50, Loss: 4.27364
INFO:root:Validation iteration 60, Loss: 4.29657
INFO:root:Validation iteration 70, Loss: 4.31058
INFO:root:Validation iteration 80, Loss: 4.22871
INFO:root:Validation iteration 90, Loss: 4.27118
INFO:root:Validation iteration 100, Loss: 4.31403
INFO:root:Validation iteration 110, Loss: 4.23120
INFO:root:Validation iteration 120, Loss: 4.30827
INFO:root:Validation iteration 130, Loss: 4.21650
Test accuracy: 0.104, Test loss: 4.27618
INFO:root:Saving results...
INFO:root:Done!
"""

string11="""
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=32, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/398
INFO:root:Processing batch 2/398
INFO:root:Processing batch 3/398
INFO:root:Processing batch 4/398
INFO:root:Processing batch 5/398
INFO:root:Processing batch 6/398
INFO:root:Processing batch 7/398
INFO:root:Processing batch 8/398
INFO:root:Processing batch 9/398
INFO:root:Processing batch 10/398
INFO:root:Processing batch 11/398
INFO:root:Processing batch 12/398
INFO:root:Processing batch 13/398
INFO:root:Processing batch 14/398
INFO:root:Processing batch 15/398
INFO:root:Processing batch 16/398
INFO:root:Processing batch 17/398
INFO:root:Processing batch 18/398
INFO:root:Processing batch 19/398
INFO:root:Processing batch 20/398
INFO:root:Processing batch 21/398
INFO:root:Processing batch 22/398
INFO:root:Processing batch 23/398
INFO:root:Processing batch 24/398
INFO:root:Processing batch 25/398
INFO:root:Processing batch 26/398
INFO:root:Processing batch 27/398
INFO:root:Processing batch 28/398
INFO:root:Processing batch 29/398
INFO:root:Processing batch 30/398
INFO:root:Processing batch 31/398
INFO:root:Processing batch 32/398
INFO:root:Processing batch 33/398
INFO:root:Processing batch 34/398
INFO:root:Processing batch 35/398
INFO:root:Processing batch 36/398
INFO:root:Processing batch 37/398
INFO:root:Processing batch 38/398
INFO:root:Processing batch 39/398
INFO:root:Processing batch 40/398
INFO:root:Processing batch 41/398
INFO:root:Processing batch 42/398
INFO:root:Processing batch 43/398
INFO:root:Processing batch 44/398
INFO:root:Processing batch 45/398
INFO:root:Processing batch 46/398
INFO:root:Processing batch 47/398
INFO:root:Processing batch 48/398
INFO:root:Processing batch 49/398
INFO:root:Processing batch 50/398
INFO:root:Processing batch 51/398
INFO:root:Processing batch 52/398
INFO:root:Processing batch 53/398
INFO:root:Processing batch 54/398
INFO:root:Processing batch 55/398
INFO:root:Processing batch 56/398
INFO:root:Processing batch 57/398
INFO:root:Processing batch 58/398
INFO:root:Processing batch 59/398
INFO:root:Processing batch 60/398
INFO:root:Processing batch 61/398
INFO:root:Processing batch 62/398
INFO:root:Processing batch 63/398
INFO:root:Processing batch 64/398
INFO:root:Processing batch 65/398
INFO:root:Processing batch 66/398
INFO:root:Processing batch 67/398
INFO:root:Processing batch 68/398
INFO:root:Processing batch 69/398
INFO:root:Processing batch 70/398
INFO:root:Processing batch 71/398
INFO:root:Processing batch 72/398
INFO:root:Processing batch 73/398
INFO:root:Processing batch 74/398
INFO:root:Processing batch 75/398
INFO:root:Processing batch 76/398
INFO:root:Processing batch 77/398
INFO:root:Processing batch 78/398
INFO:root:Processing batch 79/398
INFO:root:Processing batch 80/398
INFO:root:Processing batch 81/398
INFO:root:Processing batch 82/398
INFO:root:Processing batch 83/398
INFO:root:Processing batch 84/398
INFO:root:Processing batch 85/398
INFO:root:Processing batch 86/398
INFO:root:Processing batch 87/398
INFO:root:Processing batch 88/398
INFO:root:Processing batch 89/398
INFO:root:Processing batch 90/398
INFO:root:Processing batch 91/398
INFO:root:Processing batch 92/398
INFO:root:Processing batch 93/398
INFO:root:Processing batch 94/398
INFO:root:Processing batch 95/398
INFO:root:Processing batch 96/398
INFO:root:Processing batch 97/398
INFO:root:Processing batch 98/398
INFO:root:Processing batch 99/398
INFO:root:Processing batch 100/398
INFO:root:Processing batch 101/398
INFO:root:Processing batch 102/398
INFO:root:Processing batch 103/398
INFO:root:Processing batch 104/398
INFO:root:Processing batch 105/398
INFO:root:Processing batch 106/398
INFO:root:Processing batch 107/398
INFO:root:Processing batch 108/398
INFO:root:Processing batch 109/398
INFO:root:Processing batch 110/398
INFO:root:Processing batch 111/398
INFO:root:Processing batch 112/398
INFO:root:Processing batch 113/398
INFO:root:Processing batch 114/398
INFO:root:Processing batch 115/398
INFO:root:Processing batch 116/398
INFO:root:Processing batch 117/398
INFO:root:Processing batch 118/398
INFO:root:Processing batch 119/398
INFO:root:Processing batch 120/398
INFO:root:Processing batch 121/398
INFO:root:Processing batch 122/398
INFO:root:Processing batch 123/398
INFO:root:Processing batch 124/398
INFO:root:Processing batch 125/398
INFO:root:Processing batch 126/398
INFO:root:Processing batch 127/398
INFO:root:Processing batch 128/398
INFO:root:Processing batch 129/398
INFO:root:Processing batch 130/398
INFO:root:Processing batch 131/398
INFO:root:Processing batch 132/398
INFO:root:Processing batch 133/398
INFO:root:Processing batch 134/398
INFO:root:Processing batch 135/398
INFO:root:Processing batch 136/398
INFO:root:Processing batch 137/398
INFO:root:Processing batch 138/398
INFO:root:Processing batch 139/398
INFO:root:Processing batch 140/398
INFO:root:Processing batch 141/398
INFO:root:Processing batch 142/398
INFO:root:Processing batch 143/398
INFO:root:Processing batch 144/398
INFO:root:Processing batch 145/398
INFO:root:Processing batch 146/398
INFO:root:Processing batch 147/398
INFO:root:Processing batch 148/398
INFO:root:Processing batch 149/398
INFO:root:Processing batch 150/398
INFO:root:Processing batch 151/398
INFO:root:Processing batch 152/398
INFO:root:Processing batch 153/398
INFO:root:Processing batch 154/398
INFO:root:Processing batch 155/398
INFO:root:Processing batch 156/398
INFO:root:Processing batch 157/398
INFO:root:Processing batch 158/398
INFO:root:Processing batch 159/398
INFO:root:Processing batch 160/398
INFO:root:Processing batch 161/398
INFO:root:Processing batch 162/398
INFO:root:Processing batch 163/398
INFO:root:Processing batch 164/398
INFO:root:Processing batch 165/398
INFO:root:Processing batch 166/398
INFO:root:Processing batch 167/398
INFO:root:Processing batch 168/398
INFO:root:Processing batch 169/398
INFO:root:Processing batch 170/398
INFO:root:Processing batch 171/398
INFO:root:Processing batch 172/398
INFO:root:Processing batch 173/398
INFO:root:Processing batch 174/398
INFO:root:Processing batch 175/398
INFO:root:Processing batch 176/398
INFO:root:Processing batch 177/398
INFO:root:Processing batch 178/398
INFO:root:Processing batch 179/398
INFO:root:Processing batch 180/398
INFO:root:Processing batch 181/398
INFO:root:Processing batch 182/398
INFO:root:Processing batch 183/398
INFO:root:Processing batch 184/398
INFO:root:Processing batch 185/398
INFO:root:Processing batch 186/398
INFO:root:Processing batch 187/398
INFO:root:Processing batch 188/398
INFO:root:Processing batch 189/398
INFO:root:Processing batch 190/398
INFO:root:Processing batch 191/398
INFO:root:Processing batch 192/398
INFO:root:Processing batch 193/398
INFO:root:Processing batch 194/398
INFO:root:Processing batch 195/398
INFO:root:Processing batch 196/398
INFO:root:Processing batch 197/398
INFO:root:Processing batch 198/398
INFO:root:Processing batch 199/398
INFO:root:Processing batch 200/398
INFO:root:Processing batch 201/398
INFO:root:Processing batch 202/398
INFO:root:Processing batch 203/398
INFO:root:Processing batch 204/398
INFO:root:Processing batch 205/398
INFO:root:Processing batch 206/398
INFO:root:Processing batch 207/398
INFO:root:Processing batch 208/398
INFO:root:Processing batch 209/398
INFO:root:Processing batch 210/398
INFO:root:Processing batch 211/398
INFO:root:Processing batch 212/398
INFO:root:Processing batch 213/398
INFO:root:Processing batch 214/398
INFO:root:Processing batch 215/398
INFO:root:Processing batch 216/398
INFO:root:Processing batch 217/398
INFO:root:Processing batch 218/398
INFO:root:Processing batch 219/398
INFO:root:Processing batch 220/398
INFO:root:Processing batch 221/398
INFO:root:Processing batch 222/398
INFO:root:Processing batch 223/398
INFO:root:Processing batch 224/398
INFO:root:Processing batch 225/398
INFO:root:Processing batch 226/398
INFO:root:Processing batch 227/398
INFO:root:Processing batch 228/398
INFO:root:Processing batch 229/398
INFO:root:Processing batch 230/398
INFO:root:Processing batch 231/398
INFO:root:Processing batch 232/398
INFO:root:Processing batch 233/398
INFO:root:Processing batch 234/398
INFO:root:Processing batch 235/398
INFO:root:Processing batch 236/398
INFO:root:Processing batch 237/398
INFO:root:Processing batch 238/398
INFO:root:Processing batch 239/398
INFO:root:Processing batch 240/398
INFO:root:Processing batch 241/398
INFO:root:Processing batch 242/398
INFO:root:Processing batch 243/398
INFO:root:Processing batch 244/398
INFO:root:Processing batch 245/398
INFO:root:Processing batch 246/398
INFO:root:Processing batch 247/398
INFO:root:Processing batch 248/398
INFO:root:Processing batch 249/398
INFO:root:Processing batch 250/398
INFO:root:Processing batch 251/398
INFO:root:Processing batch 252/398
INFO:root:Processing batch 253/398
INFO:root:Processing batch 254/398
INFO:root:Processing batch 255/398
INFO:root:Processing batch 256/398
INFO:root:Processing batch 257/398
INFO:root:Processing batch 258/398
INFO:root:Processing batch 259/398
INFO:root:Processing batch 260/398
INFO:root:Processing batch 261/398
INFO:root:Processing batch 262/398
INFO:root:Processing batch 263/398
INFO:root:Processing batch 264/398
INFO:root:Processing batch 265/398
INFO:root:Processing batch 266/398
INFO:root:Processing batch 267/398
INFO:root:Processing batch 268/398
INFO:root:Processing batch 269/398
INFO:root:Processing batch 270/398
INFO:root:Processing batch 271/398
INFO:root:Processing batch 272/398
INFO:root:Processing batch 273/398
INFO:root:Processing batch 274/398
INFO:root:Processing batch 275/398
INFO:root:Processing batch 276/398
INFO:root:Processing batch 277/398
INFO:root:Processing batch 278/398
INFO:root:Processing batch 279/398
INFO:root:Processing batch 280/398
INFO:root:Processing batch 281/398
INFO:root:Processing batch 282/398
INFO:root:Processing batch 283/398
INFO:root:Processing batch 284/398
INFO:root:Processing batch 285/398
INFO:root:Processing batch 286/398
INFO:root:Processing batch 287/398
INFO:root:Processing batch 288/398
INFO:root:Processing batch 289/398
INFO:root:Processing batch 290/398
INFO:root:Processing batch 291/398
INFO:root:Processing batch 292/398
INFO:root:Processing batch 293/398
INFO:root:Processing batch 294/398
INFO:root:Processing batch 295/398
INFO:root:Processing batch 296/398
INFO:root:Processing batch 297/398
INFO:root:Processing batch 298/398
INFO:root:Processing batch 299/398
INFO:root:Processing batch 300/398
INFO:root:Processing batch 301/398
INFO:root:Processing batch 302/398
INFO:root:Processing batch 303/398
INFO:root:Processing batch 304/398
INFO:root:Processing batch 305/398
INFO:root:Processing batch 306/398
INFO:root:Processing batch 307/398
INFO:root:Processing batch 308/398
INFO:root:Processing batch 309/398
INFO:root:Processing batch 310/398
INFO:root:Processing batch 311/398
INFO:root:Processing batch 312/398
INFO:root:Processing batch 313/398
INFO:root:Processing batch 314/398
INFO:root:Processing batch 315/398
INFO:root:Processing batch 316/398
INFO:root:Processing batch 317/398
INFO:root:Processing batch 318/398
INFO:root:Processing batch 319/398
INFO:root:Processing batch 320/398
INFO:root:Processing batch 321/398
INFO:root:Processing batch 322/398
INFO:root:Processing batch 323/398
INFO:root:Processing batch 324/398
INFO:root:Processing batch 325/398
INFO:root:Processing batch 326/398
INFO:root:Processing batch 327/398
INFO:root:Processing batch 328/398
INFO:root:Processing batch 329/398
INFO:root:Processing batch 330/398
INFO:root:Processing batch 331/398
INFO:root:Processing batch 332/398
INFO:root:Processing batch 333/398
INFO:root:Processing batch 334/398
INFO:root:Processing batch 335/398
INFO:root:Processing batch 336/398
INFO:root:Processing batch 337/398
INFO:root:Processing batch 338/398
INFO:root:Processing batch 339/398
INFO:root:Processing batch 340/398
INFO:root:Processing batch 341/398
INFO:root:Processing batch 342/398
INFO:root:Processing batch 343/398
INFO:root:Processing batch 344/398
INFO:root:Processing batch 345/398
INFO:root:Processing batch 346/398
INFO:root:Processing batch 347/398
INFO:root:Processing batch 348/398
INFO:root:Processing batch 349/398
INFO:root:Processing batch 350/398
INFO:root:Processing batch 351/398
INFO:root:Processing batch 352/398
INFO:root:Processing batch 353/398
INFO:root:Processing batch 354/398
INFO:root:Processing batch 355/398
INFO:root:Processing batch 356/398
INFO:root:Processing batch 357/398
INFO:root:Processing batch 358/398
INFO:root:Processing batch 359/398
INFO:root:Processing batch 360/398
INFO:root:Processing batch 361/398
INFO:root:Processing batch 362/398
INFO:root:Processing batch 363/398
INFO:root:Processing batch 364/398
INFO:root:Processing batch 365/398
INFO:root:Processing batch 366/398
INFO:root:Processing batch 367/398
INFO:root:Processing batch 368/398
INFO:root:Processing batch 369/398
INFO:root:Processing batch 370/398
INFO:root:Processing batch 371/398
INFO:root:Processing batch 372/398
INFO:root:Processing batch 373/398
INFO:root:Processing batch 374/398
INFO:root:Processing batch 375/398
INFO:root:Processing batch 376/398
INFO:root:Processing batch 377/398
INFO:root:Processing batch 378/398
INFO:root:Processing batch 379/398
INFO:root:Processing batch 380/398
INFO:root:Processing batch 381/398
INFO:root:Processing batch 382/398
INFO:root:Processing batch 383/398
INFO:root:Processing batch 384/398
INFO:root:Processing batch 385/398
INFO:root:Processing batch 386/398
INFO:root:Processing batch 387/398
INFO:root:Processing batch 388/398
INFO:root:Processing batch 389/398
INFO:root:Processing batch 390/398
INFO:root:Processing batch 391/398
INFO:root:Processing batch 392/398
INFO:root:Processing batch 393/398
INFO:root:Processing batch 394/398
INFO:root:Processing batch 395/398
INFO:root:Processing batch 396/398
INFO:root:Processing batch 397/398
INFO:root:Processing batch 398/398
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47586774826049805, 0.42080193758010864, 0.36042824387550354], 'std': [0.2790556848049164, 0.27419695258140564, 0.2640022039413452], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47586774826049805, 0.42080193758010864, 0.36042824387550354], std=[0.2790556848049164, 0.27419695258140564, 0.2640022039413452])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.14136
INFO:root:Training epoch 1, Iteration 30, Loss: 4.98651
INFO:root:Training epoch 1, Iteration 60, Loss: 4.75115
INFO:root:Training epoch 1, Iteration 90, Loss: 4.64781
INFO:root:Training epoch 1, Iteration 120, Loss: 4.62550
INFO:root:Training epoch 1, Iteration 150, Loss: 4.48592
INFO:root:Training epoch 1, Iteration 180, Loss: 4.49439
INFO:root:Training epoch 1, Iteration 210, Loss: 4.42976
INFO:root:Training epoch 1, Iteration 240, Loss: 4.42370
INFO:root:Training epoch 1, Iteration 270, Loss: 4.30764
INFO:root:Training epoch 1, Iteration 300, Loss: 4.29130
INFO:root:Training epoch 1, Iteration 330, Loss: 4.27408
INFO:root:Training epoch 1, Iteration 360, Loss: 4.28834
INFO:root:Training epoch 1, Iteration 390, Loss: 4.13151
INFO:root:Validation iteration 1, Loss: 3.39373
INFO:root:Validation iteration 10, Loss: 4.04064
INFO:root:Validation iteration 20, Loss: 4.13732
INFO:root:Validation iteration 30, Loss: 4.00803
INFO:root:Validation iteration 40, Loss: 4.29043
INFO:root:Validation iteration 50, Loss: 4.33883
INFO:root:Validation iteration 60, Loss: 4.05981
INFO:root:Validation iteration 70, Loss: 4.18588
INFO:root:Validation iteration 80, Loss: 4.35738
INFO:root:Validation iteration 90, Loss: 4.27873
INFO:root:Validation iteration 100, Loss: 3.98093
INFO:root:Validation iteration 110, Loss: 4.20789
INFO:root:Validation iteration 120, Loss: 4.28253
INFO:root:Validation iteration 130, Loss: 4.27081
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.465
INFO:root:Validation accuracy: 0.077, Validation loss: 4.18838
INFO:root:Training epoch 2, Iteration 1, Loss: 4.24371
INFO:root:Training epoch 2, Iteration 30, Loss: 4.11170
INFO:root:Training epoch 2, Iteration 60, Loss: 4.08535
INFO:root:Training epoch 2, Iteration 90, Loss: 4.01907
INFO:root:Training epoch 2, Iteration 120, Loss: 4.05144
INFO:root:Training epoch 2, Iteration 150, Loss: 4.06068
INFO:root:Training epoch 2, Iteration 180, Loss: 3.98196
INFO:root:Training epoch 2, Iteration 210, Loss: 3.87460
INFO:root:Training epoch 2, Iteration 240, Loss: 3.89603
INFO:root:Training epoch 2, Iteration 270, Loss: 3.90914
INFO:root:Training epoch 2, Iteration 300, Loss: 3.89407
INFO:root:Training epoch 2, Iteration 330, Loss: 3.82509
INFO:root:Training epoch 2, Iteration 360, Loss: 3.94015
INFO:root:Training epoch 2, Iteration 390, Loss: 3.99012
INFO:root:Validation iteration 1, Loss: 3.19661
INFO:root:Validation iteration 10, Loss: 3.63814
INFO:root:Validation iteration 20, Loss: 3.71611
INFO:root:Validation iteration 30, Loss: 3.82266
INFO:root:Validation iteration 40, Loss: 3.98203
INFO:root:Validation iteration 50, Loss: 3.94737
INFO:root:Validation iteration 60, Loss: 3.71349
INFO:root:Validation iteration 70, Loss: 3.78551
INFO:root:Validation iteration 80, Loss: 3.94900
INFO:root:Validation iteration 90, Loss: 3.88408
INFO:root:Validation iteration 100, Loss: 3.67648
INFO:root:Validation iteration 110, Loss: 3.85170
INFO:root:Validation iteration 120, Loss: 4.00388
INFO:root:Validation iteration 130, Loss: 3.92991
INFO:root:End of Epoch 2
INFO:root:Training loss: 3.967
INFO:root:Validation accuracy: 0.120, Validation loss: 3.84045
INFO:root:Best validation accuracy: 0.120 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.55198
INFO:root:Validation iteration 10, Loss: 3.73024
INFO:root:Validation iteration 20, Loss: 3.87275
INFO:root:Validation iteration 30, Loss: 3.84884
INFO:root:Validation iteration 40, Loss: 3.87305
INFO:root:Validation iteration 50, Loss: 3.85744
INFO:root:Validation iteration 60, Loss: 3.80043
INFO:root:Validation iteration 70, Loss: 3.77872
INFO:root:Validation iteration 80, Loss: 3.83031
INFO:root:Validation iteration 90, Loss: 3.79559
INFO:root:Validation iteration 100, Loss: 3.91777
INFO:root:Validation iteration 110, Loss: 3.81856
INFO:root:Validation iteration 120, Loss: 3.88324
INFO:root:Validation iteration 130, Loss: 3.68883
Test accuracy: 0.184, Test loss: 3.82109
INFO:root:Saving results...
INFO:root:Done!
"""

string12 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=32, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=25, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='weighted_cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/398
INFO:root:Processing batch 2/398
INFO:root:Processing batch 3/398
INFO:root:Processing batch 4/398
INFO:root:Processing batch 5/398
INFO:root:Processing batch 6/398
INFO:root:Processing batch 7/398
INFO:root:Processing batch 8/398
INFO:root:Processing batch 9/398
INFO:root:Processing batch 10/398
INFO:root:Processing batch 11/398
INFO:root:Processing batch 12/398
INFO:root:Processing batch 13/398
INFO:root:Processing batch 14/398
INFO:root:Processing batch 15/398
INFO:root:Processing batch 16/398
INFO:root:Processing batch 17/398
INFO:root:Processing batch 18/398
INFO:root:Processing batch 19/398
INFO:root:Processing batch 20/398
INFO:root:Processing batch 21/398
INFO:root:Processing batch 22/398
INFO:root:Processing batch 23/398
INFO:root:Processing batch 24/398
INFO:root:Processing batch 25/398
INFO:root:Processing batch 26/398
INFO:root:Processing batch 27/398
INFO:root:Processing batch 28/398
INFO:root:Processing batch 29/398
INFO:root:Processing batch 30/398
INFO:root:Processing batch 31/398
INFO:root:Processing batch 32/398
INFO:root:Processing batch 33/398
INFO:root:Processing batch 34/398
INFO:root:Processing batch 35/398
INFO:root:Processing batch 36/398
INFO:root:Processing batch 37/398
INFO:root:Processing batch 38/398
INFO:root:Processing batch 39/398
INFO:root:Processing batch 40/398
INFO:root:Processing batch 41/398
INFO:root:Processing batch 42/398
INFO:root:Processing batch 43/398
INFO:root:Processing batch 44/398
INFO:root:Processing batch 45/398
INFO:root:Processing batch 46/398
INFO:root:Processing batch 47/398
INFO:root:Processing batch 48/398
INFO:root:Processing batch 49/398
INFO:root:Processing batch 50/398
INFO:root:Processing batch 51/398
INFO:root:Processing batch 52/398
INFO:root:Processing batch 53/398
INFO:root:Processing batch 54/398
INFO:root:Processing batch 55/398
INFO:root:Processing batch 56/398
INFO:root:Processing batch 57/398
INFO:root:Processing batch 58/398
INFO:root:Processing batch 59/398
INFO:root:Processing batch 60/398
INFO:root:Processing batch 61/398
INFO:root:Processing batch 62/398
INFO:root:Processing batch 63/398
INFO:root:Processing batch 64/398
INFO:root:Processing batch 65/398
INFO:root:Processing batch 66/398
INFO:root:Processing batch 67/398
INFO:root:Processing batch 68/398
INFO:root:Processing batch 69/398
INFO:root:Processing batch 70/398
INFO:root:Processing batch 71/398
INFO:root:Processing batch 72/398
INFO:root:Processing batch 73/398
INFO:root:Processing batch 74/398
INFO:root:Processing batch 75/398
INFO:root:Processing batch 76/398
INFO:root:Processing batch 77/398
INFO:root:Processing batch 78/398
INFO:root:Processing batch 79/398
INFO:root:Processing batch 80/398
INFO:root:Processing batch 81/398
INFO:root:Processing batch 82/398
INFO:root:Processing batch 83/398
INFO:root:Processing batch 84/398
INFO:root:Processing batch 85/398
INFO:root:Processing batch 86/398
INFO:root:Processing batch 87/398
INFO:root:Processing batch 88/398
INFO:root:Processing batch 89/398
INFO:root:Processing batch 90/398
INFO:root:Processing batch 91/398
INFO:root:Processing batch 92/398
INFO:root:Processing batch 93/398
INFO:root:Processing batch 94/398
INFO:root:Processing batch 95/398
INFO:root:Processing batch 96/398
INFO:root:Processing batch 97/398
INFO:root:Processing batch 98/398
INFO:root:Processing batch 99/398
INFO:root:Processing batch 100/398
INFO:root:Processing batch 101/398
INFO:root:Processing batch 102/398
INFO:root:Processing batch 103/398
INFO:root:Processing batch 104/398
INFO:root:Processing batch 105/398
INFO:root:Processing batch 106/398
INFO:root:Processing batch 107/398
INFO:root:Processing batch 108/398
INFO:root:Processing batch 109/398
INFO:root:Processing batch 110/398
INFO:root:Processing batch 111/398
INFO:root:Processing batch 112/398
INFO:root:Processing batch 113/398
INFO:root:Processing batch 114/398
INFO:root:Processing batch 115/398
INFO:root:Processing batch 116/398
INFO:root:Processing batch 117/398
INFO:root:Processing batch 118/398
INFO:root:Processing batch 119/398
INFO:root:Processing batch 120/398
INFO:root:Processing batch 121/398
INFO:root:Processing batch 122/398
INFO:root:Processing batch 123/398
INFO:root:Processing batch 124/398
INFO:root:Processing batch 125/398
INFO:root:Processing batch 126/398
INFO:root:Processing batch 127/398
INFO:root:Processing batch 128/398
INFO:root:Processing batch 129/398
INFO:root:Processing batch 130/398
INFO:root:Processing batch 131/398
INFO:root:Processing batch 132/398
INFO:root:Processing batch 133/398
INFO:root:Processing batch 134/398
INFO:root:Processing batch 135/398
INFO:root:Processing batch 136/398
INFO:root:Processing batch 137/398
INFO:root:Processing batch 138/398
INFO:root:Processing batch 139/398
INFO:root:Processing batch 140/398
INFO:root:Processing batch 141/398
INFO:root:Processing batch 142/398
INFO:root:Processing batch 143/398
INFO:root:Processing batch 144/398
INFO:root:Processing batch 145/398
INFO:root:Processing batch 146/398
INFO:root:Processing batch 147/398
INFO:root:Processing batch 148/398
INFO:root:Processing batch 149/398
INFO:root:Processing batch 150/398
INFO:root:Processing batch 151/398
INFO:root:Processing batch 152/398
INFO:root:Processing batch 153/398
INFO:root:Processing batch 154/398
INFO:root:Processing batch 155/398
INFO:root:Processing batch 156/398
INFO:root:Processing batch 157/398
INFO:root:Processing batch 158/398
INFO:root:Processing batch 159/398
INFO:root:Processing batch 160/398
INFO:root:Processing batch 161/398
INFO:root:Processing batch 162/398
INFO:root:Processing batch 163/398
INFO:root:Processing batch 164/398
INFO:root:Processing batch 165/398
INFO:root:Processing batch 166/398
INFO:root:Processing batch 167/398
INFO:root:Processing batch 168/398
INFO:root:Processing batch 169/398
INFO:root:Processing batch 170/398
INFO:root:Processing batch 171/398
INFO:root:Processing batch 172/398
INFO:root:Processing batch 173/398
INFO:root:Processing batch 174/398
INFO:root:Processing batch 175/398
INFO:root:Processing batch 176/398
INFO:root:Processing batch 177/398
INFO:root:Processing batch 178/398
INFO:root:Processing batch 179/398
INFO:root:Processing batch 180/398
INFO:root:Processing batch 181/398
INFO:root:Processing batch 182/398
INFO:root:Processing batch 183/398
INFO:root:Processing batch 184/398
INFO:root:Processing batch 185/398
INFO:root:Processing batch 186/398
INFO:root:Processing batch 187/398
INFO:root:Processing batch 188/398
INFO:root:Processing batch 189/398
INFO:root:Processing batch 190/398
INFO:root:Processing batch 191/398
INFO:root:Processing batch 192/398
INFO:root:Processing batch 193/398
INFO:root:Processing batch 194/398
INFO:root:Processing batch 195/398
INFO:root:Processing batch 196/398
INFO:root:Processing batch 197/398
INFO:root:Processing batch 198/398
INFO:root:Processing batch 199/398
INFO:root:Processing batch 200/398
INFO:root:Processing batch 201/398
INFO:root:Processing batch 202/398
INFO:root:Processing batch 203/398
INFO:root:Processing batch 204/398
INFO:root:Processing batch 205/398
INFO:root:Processing batch 206/398
INFO:root:Processing batch 207/398
INFO:root:Processing batch 208/398
INFO:root:Processing batch 209/398
INFO:root:Processing batch 210/398
INFO:root:Processing batch 211/398
INFO:root:Processing batch 212/398
INFO:root:Processing batch 213/398
INFO:root:Processing batch 214/398
INFO:root:Processing batch 215/398
INFO:root:Processing batch 216/398
INFO:root:Processing batch 217/398
INFO:root:Processing batch 218/398
INFO:root:Processing batch 219/398
INFO:root:Processing batch 220/398
INFO:root:Processing batch 221/398
INFO:root:Processing batch 222/398
INFO:root:Processing batch 223/398
INFO:root:Processing batch 224/398
INFO:root:Processing batch 225/398
INFO:root:Processing batch 226/398
INFO:root:Processing batch 227/398
INFO:root:Processing batch 228/398
INFO:root:Processing batch 229/398
INFO:root:Processing batch 230/398
INFO:root:Processing batch 231/398
INFO:root:Processing batch 232/398
INFO:root:Processing batch 233/398
INFO:root:Processing batch 234/398
INFO:root:Processing batch 235/398
INFO:root:Processing batch 236/398
INFO:root:Processing batch 237/398
INFO:root:Processing batch 238/398
INFO:root:Processing batch 239/398
INFO:root:Processing batch 240/398
INFO:root:Processing batch 241/398
INFO:root:Processing batch 242/398
INFO:root:Processing batch 243/398
INFO:root:Processing batch 244/398
INFO:root:Processing batch 245/398
INFO:root:Processing batch 246/398
INFO:root:Processing batch 247/398
INFO:root:Processing batch 248/398
INFO:root:Processing batch 249/398
INFO:root:Processing batch 250/398
INFO:root:Processing batch 251/398
INFO:root:Processing batch 252/398
INFO:root:Processing batch 253/398
INFO:root:Processing batch 254/398
INFO:root:Processing batch 255/398
INFO:root:Processing batch 256/398
INFO:root:Processing batch 257/398
INFO:root:Processing batch 258/398
INFO:root:Processing batch 259/398
INFO:root:Processing batch 260/398
INFO:root:Processing batch 261/398
INFO:root:Processing batch 262/398
INFO:root:Processing batch 263/398
INFO:root:Processing batch 264/398
INFO:root:Processing batch 265/398
INFO:root:Processing batch 266/398
INFO:root:Processing batch 267/398
INFO:root:Processing batch 268/398
INFO:root:Processing batch 269/398
INFO:root:Processing batch 270/398
INFO:root:Processing batch 271/398
INFO:root:Processing batch 272/398
INFO:root:Processing batch 273/398
INFO:root:Processing batch 274/398
INFO:root:Processing batch 275/398
INFO:root:Processing batch 276/398
INFO:root:Processing batch 277/398
INFO:root:Processing batch 278/398
INFO:root:Processing batch 279/398
INFO:root:Processing batch 280/398
INFO:root:Processing batch 281/398
INFO:root:Processing batch 282/398
INFO:root:Processing batch 283/398
INFO:root:Processing batch 284/398
INFO:root:Processing batch 285/398
INFO:root:Processing batch 286/398
INFO:root:Processing batch 287/398
INFO:root:Processing batch 288/398
INFO:root:Processing batch 289/398
INFO:root:Processing batch 290/398
INFO:root:Processing batch 291/398
INFO:root:Processing batch 292/398
INFO:root:Processing batch 293/398
INFO:root:Processing batch 294/398
INFO:root:Processing batch 295/398
INFO:root:Processing batch 296/398
INFO:root:Processing batch 297/398
INFO:root:Processing batch 298/398
INFO:root:Processing batch 299/398
INFO:root:Processing batch 300/398
INFO:root:Processing batch 301/398
INFO:root:Processing batch 302/398
INFO:root:Processing batch 303/398
INFO:root:Processing batch 304/398
INFO:root:Processing batch 305/398
INFO:root:Processing batch 306/398
INFO:root:Processing batch 307/398
INFO:root:Processing batch 308/398
INFO:root:Processing batch 309/398
INFO:root:Processing batch 310/398
INFO:root:Processing batch 311/398
INFO:root:Processing batch 312/398
INFO:root:Processing batch 313/398
INFO:root:Processing batch 314/398
INFO:root:Processing batch 315/398
INFO:root:Processing batch 316/398
INFO:root:Processing batch 317/398
INFO:root:Processing batch 318/398
INFO:root:Processing batch 319/398
INFO:root:Processing batch 320/398
INFO:root:Processing batch 321/398
INFO:root:Processing batch 322/398
INFO:root:Processing batch 323/398
INFO:root:Processing batch 324/398
INFO:root:Processing batch 325/398
INFO:root:Processing batch 326/398
INFO:root:Processing batch 327/398
INFO:root:Processing batch 328/398
INFO:root:Processing batch 329/398
INFO:root:Processing batch 330/398
INFO:root:Processing batch 331/398
INFO:root:Processing batch 332/398
INFO:root:Processing batch 333/398
INFO:root:Processing batch 334/398
INFO:root:Processing batch 335/398
INFO:root:Processing batch 336/398
INFO:root:Processing batch 337/398
INFO:root:Processing batch 338/398
INFO:root:Processing batch 339/398
INFO:root:Processing batch 340/398
INFO:root:Processing batch 341/398
INFO:root:Processing batch 342/398
INFO:root:Processing batch 343/398
INFO:root:Processing batch 344/398
INFO:root:Processing batch 345/398
INFO:root:Processing batch 346/398
INFO:root:Processing batch 347/398
INFO:root:Processing batch 348/398
INFO:root:Processing batch 349/398
INFO:root:Processing batch 350/398
INFO:root:Processing batch 351/398
INFO:root:Processing batch 352/398
INFO:root:Processing batch 353/398
INFO:root:Processing batch 354/398
INFO:root:Processing batch 355/398
INFO:root:Processing batch 356/398
INFO:root:Processing batch 357/398
INFO:root:Processing batch 358/398
INFO:root:Processing batch 359/398
INFO:root:Processing batch 360/398
INFO:root:Processing batch 361/398
INFO:root:Processing batch 362/398
INFO:root:Processing batch 363/398
INFO:root:Processing batch 364/398
INFO:root:Processing batch 365/398
INFO:root:Processing batch 366/398
INFO:root:Processing batch 367/398
INFO:root:Processing batch 368/398
INFO:root:Processing batch 369/398
INFO:root:Processing batch 370/398
INFO:root:Processing batch 371/398
INFO:root:Processing batch 372/398
INFO:root:Processing batch 373/398
INFO:root:Processing batch 374/398
INFO:root:Processing batch 375/398
INFO:root:Processing batch 376/398
INFO:root:Processing batch 377/398
INFO:root:Processing batch 378/398
INFO:root:Processing batch 379/398
INFO:root:Processing batch 380/398
INFO:root:Processing batch 381/398
INFO:root:Processing batch 382/398
INFO:root:Processing batch 383/398
INFO:root:Processing batch 384/398
INFO:root:Processing batch 385/398
INFO:root:Processing batch 386/398
INFO:root:Processing batch 387/398
INFO:root:Processing batch 388/398
INFO:root:Processing batch 389/398
INFO:root:Processing batch 390/398
INFO:root:Processing batch 391/398
INFO:root:Processing batch 392/398
INFO:root:Processing batch 393/398
INFO:root:Processing batch 394/398
INFO:root:Processing batch 395/398
INFO:root:Processing batch 396/398
INFO:root:Processing batch 397/398
INFO:root:Processing batch 398/398
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47586774826049805, 0.42080193758010864, 0.36042824387550354], 'std': [0.2790556848049164, 0.27419695258140564, 0.2640022039413452], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47586774826049805, 0.42080193758010864, 0.36042824387550354], std=[0.2790556848049164, 0.27419695258140564, 0.2640022039413452])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.05017
INFO:root:Training epoch 1, Iteration 25, Loss: 5.02764
INFO:root:Training epoch 1, Iteration 50, Loss: 4.88038
INFO:root:Training epoch 1, Iteration 75, Loss: 4.76285
INFO:root:Training epoch 1, Iteration 100, Loss: 4.71192
INFO:root:Training epoch 1, Iteration 125, Loss: 4.58504
INFO:root:Training epoch 1, Iteration 150, Loss: 4.55736
INFO:root:Training epoch 1, Iteration 175, Loss: 4.46097
INFO:root:Training epoch 1, Iteration 200, Loss: 4.45313
INFO:root:Training epoch 1, Iteration 225, Loss: 4.46107
INFO:root:Training epoch 1, Iteration 250, Loss: 4.39666
INFO:root:Training epoch 1, Iteration 275, Loss: 4.28442
INFO:root:Training epoch 1, Iteration 300, Loss: 4.24334
INFO:root:Training epoch 1, Iteration 325, Loss: 4.36141
INFO:root:Training epoch 1, Iteration 350, Loss: 4.25868
INFO:root:Training epoch 1, Iteration 375, Loss: 4.29297
INFO:root:Validation iteration 1, Loss: 3.61346
INFO:root:Validation iteration 8, Loss: 4.07805
INFO:root:Validation iteration 16, Loss: 4.04223
INFO:root:Validation iteration 24, Loss: 4.22355
INFO:root:Validation iteration 32, Loss: 4.37855
INFO:root:Validation iteration 40, Loss: 4.31876
INFO:root:Validation iteration 48, Loss: 4.27785
INFO:root:Validation iteration 56, Loss: 4.08324
INFO:root:Validation iteration 64, Loss: 4.14753
INFO:root:Validation iteration 72, Loss: 4.27351
INFO:root:Validation iteration 80, Loss: 4.27217
INFO:root:Validation iteration 88, Loss: 4.18382
INFO:root:Validation iteration 96, Loss: 4.15334
INFO:root:Validation iteration 104, Loss: 4.25790
INFO:root:Validation iteration 112, Loss: 4.36106
INFO:root:Validation iteration 120, Loss: 4.32040
INFO:root:Validation iteration 128, Loss: 4.24204
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.498
INFO:root:Validation accuracy: 0.061, Validation loss: 4.22818
INFO:root:Training epoch 2, Iteration 1, Loss: 4.33660
INFO:root:Training epoch 2, Iteration 25, Loss: 4.05434
INFO:root:Training epoch 2, Iteration 50, Loss: 4.12380
INFO:root:Training epoch 2, Iteration 75, Loss: 4.11214
INFO:root:Training epoch 2, Iteration 100, Loss: 4.11467
INFO:root:Training epoch 2, Iteration 125, Loss: 4.12654
INFO:root:Training epoch 2, Iteration 150, Loss: 4.06167
INFO:root:Training epoch 2, Iteration 175, Loss: 4.04328
INFO:root:Training epoch 2, Iteration 200, Loss: 3.98129
INFO:root:Training epoch 2, Iteration 225, Loss: 4.02785
INFO:root:Training epoch 2, Iteration 250, Loss: 4.00171
INFO:root:Training epoch 2, Iteration 275, Loss: 4.01380
INFO:root:Training epoch 2, Iteration 300, Loss: 4.09421
INFO:root:Training epoch 2, Iteration 325, Loss: 3.83962
INFO:root:Training epoch 2, Iteration 350, Loss: 4.00096
INFO:root:Training epoch 2, Iteration 375, Loss: 3.91860
INFO:root:Validation iteration 1, Loss: 3.10256
INFO:root:Validation iteration 8, Loss: 3.83721
INFO:root:Validation iteration 16, Loss: 3.75139
INFO:root:Validation iteration 24, Loss: 4.01436
INFO:root:Validation iteration 32, Loss: 4.15319
INFO:root:Validation iteration 40, Loss: 3.98893
INFO:root:Validation iteration 48, Loss: 3.99329
INFO:root:Validation iteration 56, Loss: 3.96001
INFO:root:Validation iteration 64, Loss: 4.02163
INFO:root:Validation iteration 72, Loss: 4.11613
INFO:root:Validation iteration 80, Loss: 4.00213
INFO:root:Validation iteration 88, Loss: 3.93326
INFO:root:Validation iteration 96, Loss: 3.86538
INFO:root:Validation iteration 104, Loss: 3.84850
INFO:root:Validation iteration 112, Loss: 4.10578
INFO:root:Validation iteration 120, Loss: 4.10951
INFO:root:Validation iteration 128, Loss: 3.98207
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.026
INFO:root:Validation accuracy: 0.102, Validation loss: 3.98371
INFO:root:Best validation accuracy: 0.102 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.75885
INFO:root:Validation iteration 8, Loss: 3.85656
INFO:root:Validation iteration 16, Loss: 4.02431
INFO:root:Validation iteration 24, Loss: 4.11365
INFO:root:Validation iteration 32, Loss: 4.18934
INFO:root:Validation iteration 40, Loss: 4.09510
INFO:root:Validation iteration 48, Loss: 4.07620
INFO:root:Validation iteration 56, Loss: 3.83238
INFO:root:Validation iteration 64, Loss: 3.86784
INFO:root:Validation iteration 72, Loss: 3.94435
INFO:root:Validation iteration 80, Loss: 3.92253
INFO:root:Validation iteration 88, Loss: 4.01452
INFO:root:Validation iteration 96, Loss: 3.81175
INFO:root:Validation iteration 104, Loss: 3.96156
INFO:root:Validation iteration 112, Loss: 3.97012
INFO:root:Validation iteration 120, Loss: 4.05658
INFO:root:Validation iteration 128, Loss: 4.07271
Test accuracy: 0.136, Test loss: 3.98419
INFO:root:Saving results...
INFO:root:Done!
"""

string13 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=32, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=20, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/398
INFO:root:Processing batch 2/398
INFO:root:Processing batch 3/398
INFO:root:Processing batch 4/398
INFO:root:Processing batch 5/398
INFO:root:Processing batch 6/398
INFO:root:Processing batch 7/398
INFO:root:Processing batch 8/398
INFO:root:Processing batch 9/398
INFO:root:Processing batch 10/398
INFO:root:Processing batch 11/398
INFO:root:Processing batch 12/398
INFO:root:Processing batch 13/398
INFO:root:Processing batch 14/398
INFO:root:Processing batch 15/398
INFO:root:Processing batch 16/398
INFO:root:Processing batch 17/398
INFO:root:Processing batch 18/398
INFO:root:Processing batch 19/398
INFO:root:Processing batch 20/398
INFO:root:Processing batch 21/398
INFO:root:Processing batch 22/398
INFO:root:Processing batch 23/398
INFO:root:Processing batch 24/398
INFO:root:Processing batch 25/398
INFO:root:Processing batch 26/398
INFO:root:Processing batch 27/398
INFO:root:Processing batch 28/398
INFO:root:Processing batch 29/398
INFO:root:Processing batch 30/398
INFO:root:Processing batch 31/398
INFO:root:Processing batch 32/398
INFO:root:Processing batch 33/398
INFO:root:Processing batch 34/398
INFO:root:Processing batch 35/398
INFO:root:Processing batch 36/398
INFO:root:Processing batch 37/398
INFO:root:Processing batch 38/398
INFO:root:Processing batch 39/398
INFO:root:Processing batch 40/398
INFO:root:Processing batch 41/398
INFO:root:Processing batch 42/398
INFO:root:Processing batch 43/398
INFO:root:Processing batch 44/398
INFO:root:Processing batch 45/398
INFO:root:Processing batch 46/398
INFO:root:Processing batch 47/398
INFO:root:Processing batch 48/398
INFO:root:Processing batch 49/398
INFO:root:Processing batch 50/398
INFO:root:Processing batch 51/398
INFO:root:Processing batch 52/398
INFO:root:Processing batch 53/398
INFO:root:Processing batch 54/398
INFO:root:Processing batch 55/398
INFO:root:Processing batch 56/398
INFO:root:Processing batch 57/398
INFO:root:Processing batch 58/398
INFO:root:Processing batch 59/398
INFO:root:Processing batch 60/398
INFO:root:Processing batch 61/398
INFO:root:Processing batch 62/398
INFO:root:Processing batch 63/398
INFO:root:Processing batch 64/398
INFO:root:Processing batch 65/398
INFO:root:Processing batch 66/398
INFO:root:Processing batch 67/398
INFO:root:Processing batch 68/398
INFO:root:Processing batch 69/398
INFO:root:Processing batch 70/398
INFO:root:Processing batch 71/398
INFO:root:Processing batch 72/398
INFO:root:Processing batch 73/398
INFO:root:Processing batch 74/398
INFO:root:Processing batch 75/398
INFO:root:Processing batch 76/398
INFO:root:Processing batch 77/398
INFO:root:Processing batch 78/398
INFO:root:Processing batch 79/398
INFO:root:Processing batch 80/398
INFO:root:Processing batch 81/398
INFO:root:Processing batch 82/398
INFO:root:Processing batch 83/398
INFO:root:Processing batch 84/398
INFO:root:Processing batch 85/398
INFO:root:Processing batch 86/398
INFO:root:Processing batch 87/398
INFO:root:Processing batch 88/398
INFO:root:Processing batch 89/398
INFO:root:Processing batch 90/398
INFO:root:Processing batch 91/398
INFO:root:Processing batch 92/398
INFO:root:Processing batch 93/398
INFO:root:Processing batch 94/398
INFO:root:Processing batch 95/398
INFO:root:Processing batch 96/398
INFO:root:Processing batch 97/398
INFO:root:Processing batch 98/398
INFO:root:Processing batch 99/398
INFO:root:Processing batch 100/398
INFO:root:Processing batch 101/398
INFO:root:Processing batch 102/398
INFO:root:Processing batch 103/398
INFO:root:Processing batch 104/398
INFO:root:Processing batch 105/398
INFO:root:Processing batch 106/398
INFO:root:Processing batch 107/398
INFO:root:Processing batch 108/398
INFO:root:Processing batch 109/398
INFO:root:Processing batch 110/398
INFO:root:Processing batch 111/398
INFO:root:Processing batch 112/398
INFO:root:Processing batch 113/398
INFO:root:Processing batch 114/398
INFO:root:Processing batch 115/398
INFO:root:Processing batch 116/398
INFO:root:Processing batch 117/398
INFO:root:Processing batch 118/398
INFO:root:Processing batch 119/398
INFO:root:Processing batch 120/398
INFO:root:Processing batch 121/398
INFO:root:Processing batch 122/398
INFO:root:Processing batch 123/398
INFO:root:Processing batch 124/398
INFO:root:Processing batch 125/398
INFO:root:Processing batch 126/398
INFO:root:Processing batch 127/398
INFO:root:Processing batch 128/398
INFO:root:Processing batch 129/398
INFO:root:Processing batch 130/398
INFO:root:Processing batch 131/398
INFO:root:Processing batch 132/398
INFO:root:Processing batch 133/398
INFO:root:Processing batch 134/398
INFO:root:Processing batch 135/398
INFO:root:Processing batch 136/398
INFO:root:Processing batch 137/398
INFO:root:Processing batch 138/398
INFO:root:Processing batch 139/398
INFO:root:Processing batch 140/398
INFO:root:Processing batch 141/398
INFO:root:Processing batch 142/398
INFO:root:Processing batch 143/398
INFO:root:Processing batch 144/398
INFO:root:Processing batch 145/398
INFO:root:Processing batch 146/398
INFO:root:Processing batch 147/398
INFO:root:Processing batch 148/398
INFO:root:Processing batch 149/398
INFO:root:Processing batch 150/398
INFO:root:Processing batch 151/398
INFO:root:Processing batch 152/398
INFO:root:Processing batch 153/398
INFO:root:Processing batch 154/398
INFO:root:Processing batch 155/398
INFO:root:Processing batch 156/398
INFO:root:Processing batch 157/398
INFO:root:Processing batch 158/398
INFO:root:Processing batch 159/398
INFO:root:Processing batch 160/398
INFO:root:Processing batch 161/398
INFO:root:Processing batch 162/398
INFO:root:Processing batch 163/398
INFO:root:Processing batch 164/398
INFO:root:Processing batch 165/398
INFO:root:Processing batch 166/398
INFO:root:Processing batch 167/398
INFO:root:Processing batch 168/398
INFO:root:Processing batch 169/398
INFO:root:Processing batch 170/398
INFO:root:Processing batch 171/398
INFO:root:Processing batch 172/398
INFO:root:Processing batch 173/398
INFO:root:Processing batch 174/398
INFO:root:Processing batch 175/398
INFO:root:Processing batch 176/398
INFO:root:Processing batch 177/398
INFO:root:Processing batch 178/398
INFO:root:Processing batch 179/398
INFO:root:Processing batch 180/398
INFO:root:Processing batch 181/398
INFO:root:Processing batch 182/398
INFO:root:Processing batch 183/398
INFO:root:Processing batch 184/398
INFO:root:Processing batch 185/398
INFO:root:Processing batch 186/398
INFO:root:Processing batch 187/398
INFO:root:Processing batch 188/398
INFO:root:Processing batch 189/398
INFO:root:Processing batch 190/398
INFO:root:Processing batch 191/398
INFO:root:Processing batch 192/398
INFO:root:Processing batch 193/398
INFO:root:Processing batch 194/398
INFO:root:Processing batch 195/398
INFO:root:Processing batch 196/398
INFO:root:Processing batch 197/398
INFO:root:Processing batch 198/398
INFO:root:Processing batch 199/398
INFO:root:Processing batch 200/398
INFO:root:Processing batch 201/398
INFO:root:Processing batch 202/398
INFO:root:Processing batch 203/398
INFO:root:Processing batch 204/398
INFO:root:Processing batch 205/398
INFO:root:Processing batch 206/398
INFO:root:Processing batch 207/398
INFO:root:Processing batch 208/398
INFO:root:Processing batch 209/398
INFO:root:Processing batch 210/398
INFO:root:Processing batch 211/398
INFO:root:Processing batch 212/398
INFO:root:Processing batch 213/398
INFO:root:Processing batch 214/398
INFO:root:Processing batch 215/398
INFO:root:Processing batch 216/398
INFO:root:Processing batch 217/398
INFO:root:Processing batch 218/398
INFO:root:Processing batch 219/398
INFO:root:Processing batch 220/398
INFO:root:Processing batch 221/398
INFO:root:Processing batch 222/398
INFO:root:Processing batch 223/398
INFO:root:Processing batch 224/398
INFO:root:Processing batch 225/398
INFO:root:Processing batch 226/398
INFO:root:Processing batch 227/398
INFO:root:Processing batch 228/398
INFO:root:Processing batch 229/398
INFO:root:Processing batch 230/398
INFO:root:Processing batch 231/398
INFO:root:Processing batch 232/398
INFO:root:Processing batch 233/398
INFO:root:Processing batch 234/398
INFO:root:Processing batch 235/398
INFO:root:Processing batch 236/398
INFO:root:Processing batch 237/398
INFO:root:Processing batch 238/398
INFO:root:Processing batch 239/398
INFO:root:Processing batch 240/398
INFO:root:Processing batch 241/398
INFO:root:Processing batch 242/398
INFO:root:Processing batch 243/398
INFO:root:Processing batch 244/398
INFO:root:Processing batch 245/398
INFO:root:Processing batch 246/398
INFO:root:Processing batch 247/398
INFO:root:Processing batch 248/398
INFO:root:Processing batch 249/398
INFO:root:Processing batch 250/398
INFO:root:Processing batch 251/398
INFO:root:Processing batch 252/398
INFO:root:Processing batch 253/398
INFO:root:Processing batch 254/398
INFO:root:Processing batch 255/398
INFO:root:Processing batch 256/398
INFO:root:Processing batch 257/398
INFO:root:Processing batch 258/398
INFO:root:Processing batch 259/398
INFO:root:Processing batch 260/398
INFO:root:Processing batch 261/398
INFO:root:Processing batch 262/398
INFO:root:Processing batch 263/398
INFO:root:Processing batch 264/398
INFO:root:Processing batch 265/398
INFO:root:Processing batch 266/398
INFO:root:Processing batch 267/398
INFO:root:Processing batch 268/398
INFO:root:Processing batch 269/398
INFO:root:Processing batch 270/398
INFO:root:Processing batch 271/398
INFO:root:Processing batch 272/398
INFO:root:Processing batch 273/398
INFO:root:Processing batch 274/398
INFO:root:Processing batch 275/398
INFO:root:Processing batch 276/398
INFO:root:Processing batch 277/398
INFO:root:Processing batch 278/398
INFO:root:Processing batch 279/398
INFO:root:Processing batch 280/398
INFO:root:Processing batch 281/398
INFO:root:Processing batch 282/398
INFO:root:Processing batch 283/398
INFO:root:Processing batch 284/398
INFO:root:Processing batch 285/398
INFO:root:Processing batch 286/398
INFO:root:Processing batch 287/398
INFO:root:Processing batch 288/398
INFO:root:Processing batch 289/398
INFO:root:Processing batch 290/398
INFO:root:Processing batch 291/398
INFO:root:Processing batch 292/398
INFO:root:Processing batch 293/398
INFO:root:Processing batch 294/398
INFO:root:Processing batch 295/398
INFO:root:Processing batch 296/398
INFO:root:Processing batch 297/398
INFO:root:Processing batch 298/398
INFO:root:Processing batch 299/398
INFO:root:Processing batch 300/398
INFO:root:Processing batch 301/398
INFO:root:Processing batch 302/398
INFO:root:Processing batch 303/398
INFO:root:Processing batch 304/398
INFO:root:Processing batch 305/398
INFO:root:Processing batch 306/398
INFO:root:Processing batch 307/398
INFO:root:Processing batch 308/398
INFO:root:Processing batch 309/398
INFO:root:Processing batch 310/398
INFO:root:Processing batch 311/398
INFO:root:Processing batch 312/398
INFO:root:Processing batch 313/398
INFO:root:Processing batch 314/398
INFO:root:Processing batch 315/398
INFO:root:Processing batch 316/398
INFO:root:Processing batch 317/398
INFO:root:Processing batch 318/398
INFO:root:Processing batch 319/398
INFO:root:Processing batch 320/398
INFO:root:Processing batch 321/398
INFO:root:Processing batch 322/398
INFO:root:Processing batch 323/398
INFO:root:Processing batch 324/398
INFO:root:Processing batch 325/398
INFO:root:Processing batch 326/398
INFO:root:Processing batch 327/398
INFO:root:Processing batch 328/398
INFO:root:Processing batch 329/398
INFO:root:Processing batch 330/398
INFO:root:Processing batch 331/398
INFO:root:Processing batch 332/398
INFO:root:Processing batch 333/398
INFO:root:Processing batch 334/398
INFO:root:Processing batch 335/398
INFO:root:Processing batch 336/398
INFO:root:Processing batch 337/398
INFO:root:Processing batch 338/398
INFO:root:Processing batch 339/398
INFO:root:Processing batch 340/398
INFO:root:Processing batch 341/398
INFO:root:Processing batch 342/398
INFO:root:Processing batch 343/398
INFO:root:Processing batch 344/398
INFO:root:Processing batch 345/398
INFO:root:Processing batch 346/398
INFO:root:Processing batch 347/398
INFO:root:Processing batch 348/398
INFO:root:Processing batch 349/398
INFO:root:Processing batch 350/398
INFO:root:Processing batch 351/398
INFO:root:Processing batch 352/398
INFO:root:Processing batch 353/398
INFO:root:Processing batch 354/398
INFO:root:Processing batch 355/398
INFO:root:Processing batch 356/398
INFO:root:Processing batch 357/398
INFO:root:Processing batch 358/398
INFO:root:Processing batch 359/398
INFO:root:Processing batch 360/398
INFO:root:Processing batch 361/398
INFO:root:Processing batch 362/398
INFO:root:Processing batch 363/398
INFO:root:Processing batch 364/398
INFO:root:Processing batch 365/398
INFO:root:Processing batch 366/398
INFO:root:Processing batch 367/398
INFO:root:Processing batch 368/398
INFO:root:Processing batch 369/398
INFO:root:Processing batch 370/398
INFO:root:Processing batch 371/398
INFO:root:Processing batch 372/398
INFO:root:Processing batch 373/398
INFO:root:Processing batch 374/398
INFO:root:Processing batch 375/398
INFO:root:Processing batch 376/398
INFO:root:Processing batch 377/398
INFO:root:Processing batch 378/398
INFO:root:Processing batch 379/398
INFO:root:Processing batch 380/398
INFO:root:Processing batch 381/398
INFO:root:Processing batch 382/398
INFO:root:Processing batch 383/398
INFO:root:Processing batch 384/398
INFO:root:Processing batch 385/398
INFO:root:Processing batch 386/398
INFO:root:Processing batch 387/398
INFO:root:Processing batch 388/398
INFO:root:Processing batch 389/398
INFO:root:Processing batch 390/398
INFO:root:Processing batch 391/398
INFO:root:Processing batch 392/398
INFO:root:Processing batch 393/398
INFO:root:Processing batch 394/398
INFO:root:Processing batch 395/398
INFO:root:Processing batch 396/398
INFO:root:Processing batch 397/398
INFO:root:Processing batch 398/398
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4748102128505707, 0.4196726083755493, 0.3590792119503021], 'std': [0.27919745445251465, 0.27405115962028503, 0.2634221911430359], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4748102128505707, 0.4196726083755493, 0.3590792119503021], std=[0.27919745445251465, 0.27405115962028503, 0.2634221911430359])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.17533
INFO:root:Training epoch 1, Iteration 20, Loss: 4.99084
INFO:root:Training epoch 1, Iteration 40, Loss: 4.86508
INFO:root:Training epoch 1, Iteration 60, Loss: 4.71088
INFO:root:Training epoch 1, Iteration 80, Loss: 4.75057
INFO:root:Training epoch 1, Iteration 100, Loss: 4.63926
INFO:root:Training epoch 1, Iteration 120, Loss: 4.63718
INFO:root:Training epoch 1, Iteration 140, Loss: 4.45576
INFO:root:Training epoch 1, Iteration 160, Loss: 4.54138
INFO:root:Training epoch 1, Iteration 180, Loss: 4.47812
INFO:root:Training epoch 1, Iteration 200, Loss: 4.45193
INFO:root:Training epoch 1, Iteration 220, Loss: 4.38741
INFO:root:Training epoch 1, Iteration 240, Loss: 4.26640
INFO:root:Training epoch 1, Iteration 260, Loss: 4.25038
INFO:root:Training epoch 1, Iteration 280, Loss: 4.27413
INFO:root:Training epoch 1, Iteration 300, Loss: 4.35582
INFO:root:Training epoch 1, Iteration 320, Loss: 4.34708
INFO:root:Training epoch 1, Iteration 340, Loss: 4.31709
INFO:root:Training epoch 1, Iteration 360, Loss: 4.20090
INFO:root:Training epoch 1, Iteration 380, Loss: 4.23292
INFO:root:Validation iteration 1, Loss: 4.47794
INFO:root:Validation iteration 8, Loss: 4.21202
INFO:root:Validation iteration 16, Loss: 4.14461
INFO:root:Validation iteration 24, Loss: 4.22137
INFO:root:Validation iteration 32, Loss: 4.17011
INFO:root:Validation iteration 40, Loss: 4.12971
INFO:root:Validation iteration 48, Loss: 4.12067
INFO:root:Validation iteration 56, Loss: 4.22337
INFO:root:Validation iteration 64, Loss: 4.04850
INFO:root:Validation iteration 72, Loss: 4.22045
INFO:root:Validation iteration 80, Loss: 4.21478
INFO:root:Validation iteration 88, Loss: 4.24873
INFO:root:Validation iteration 96, Loss: 4.07316
INFO:root:Validation iteration 104, Loss: 4.11127
INFO:root:Validation iteration 112, Loss: 4.26435
INFO:root:Validation iteration 120, Loss: 4.23032
INFO:root:Validation iteration 128, Loss: 4.17263
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.468
INFO:root:Validation accuracy: 0.074, Validation loss: 4.17818
INFO:root:Training epoch 2, Iteration 1, Loss: 4.18389
INFO:root:Training epoch 2, Iteration 20, Loss: 4.03881
INFO:root:Training epoch 2, Iteration 40, Loss: 4.02873
INFO:root:Training epoch 2, Iteration 60, Loss: 4.10792
INFO:root:Training epoch 2, Iteration 80, Loss: 4.03052
INFO:root:Training epoch 2, Iteration 100, Loss: 4.00271
INFO:root:Training epoch 2, Iteration 120, Loss: 3.98140
INFO:root:Training epoch 2, Iteration 140, Loss: 4.05992
INFO:root:Training epoch 2, Iteration 160, Loss: 4.01285
INFO:root:Training epoch 2, Iteration 180, Loss: 4.09426
INFO:root:Training epoch 2, Iteration 200, Loss: 3.84793
INFO:root:Training epoch 2, Iteration 220, Loss: 4.01026
INFO:root:Training epoch 2, Iteration 240, Loss: 4.01403
INFO:root:Training epoch 2, Iteration 260, Loss: 3.95342
INFO:root:Training epoch 2, Iteration 280, Loss: 3.96327
INFO:root:Training epoch 2, Iteration 300, Loss: 4.00772
INFO:root:Training epoch 2, Iteration 320, Loss: 3.95498
INFO:root:Training epoch 2, Iteration 340, Loss: 3.99237
INFO:root:Training epoch 2, Iteration 360, Loss: 3.96823
INFO:root:Training epoch 2, Iteration 380, Loss: 3.92232
INFO:root:Validation iteration 1, Loss: 3.94312
INFO:root:Validation iteration 8, Loss: 3.97473
INFO:root:Validation iteration 16, Loss: 3.85293
INFO:root:Validation iteration 24, Loss: 4.00241
INFO:root:Validation iteration 32, Loss: 3.99198
INFO:root:Validation iteration 40, Loss: 3.93417
INFO:root:Validation iteration 48, Loss: 3.79321
INFO:root:Validation iteration 56, Loss: 3.92711
INFO:root:Validation iteration 64, Loss: 3.90370
INFO:root:Validation iteration 72, Loss: 3.95366
INFO:root:Validation iteration 80, Loss: 3.89963
INFO:root:Validation iteration 88, Loss: 4.03100
INFO:root:Validation iteration 96, Loss: 3.78873
INFO:root:Validation iteration 104, Loss: 3.81535
INFO:root:Validation iteration 112, Loss: 3.93443
INFO:root:Validation iteration 120, Loss: 4.00821
INFO:root:Validation iteration 128, Loss: 3.89304
INFO:root:End of Epoch 2
INFO:root:Training loss: 3.993
INFO:root:Validation accuracy: 0.107, Validation loss: 3.92236
INFO:root:Best validation accuracy: 0.107 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 4.44836
INFO:root:Validation iteration 8, Loss: 4.15866
INFO:root:Validation iteration 16, Loss: 4.10745
INFO:root:Validation iteration 24, Loss: 4.05779
INFO:root:Validation iteration 32, Loss: 3.81655
INFO:root:Validation iteration 40, Loss: 4.00042
INFO:root:Validation iteration 48, Loss: 3.89084
INFO:root:Validation iteration 56, Loss: 3.72706
INFO:root:Validation iteration 64, Loss: 3.81007
INFO:root:Validation iteration 72, Loss: 3.89399
INFO:root:Validation iteration 80, Loss: 3.73145
INFO:root:Validation iteration 88, Loss: 3.94543
INFO:root:Validation iteration 96, Loss: 3.80770
INFO:root:Validation iteration 104, Loss: 3.99132
INFO:root:Validation iteration 112, Loss: 4.03967
INFO:root:Validation iteration 120, Loss: 3.95458
INFO:root:Validation iteration 128, Loss: 3.93181
Test accuracy: 0.162, Test loss: 3.93711
INFO:root:Saving results...
INFO:root:Done!
"""

string14 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=32, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=20, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='weighted_cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/398
INFO:root:Processing batch 2/398
INFO:root:Processing batch 3/398
INFO:root:Processing batch 4/398
INFO:root:Processing batch 5/398
INFO:root:Processing batch 6/398
INFO:root:Processing batch 7/398
INFO:root:Processing batch 8/398
INFO:root:Processing batch 9/398
INFO:root:Processing batch 10/398
INFO:root:Processing batch 11/398
INFO:root:Processing batch 12/398
INFO:root:Processing batch 13/398
INFO:root:Processing batch 14/398
INFO:root:Processing batch 15/398
INFO:root:Processing batch 16/398
INFO:root:Processing batch 17/398
INFO:root:Processing batch 18/398
INFO:root:Processing batch 19/398
INFO:root:Processing batch 20/398
INFO:root:Processing batch 21/398
INFO:root:Processing batch 22/398
INFO:root:Processing batch 23/398
INFO:root:Processing batch 24/398
INFO:root:Processing batch 25/398
INFO:root:Processing batch 26/398
INFO:root:Processing batch 27/398
INFO:root:Processing batch 28/398
INFO:root:Processing batch 29/398
INFO:root:Processing batch 30/398
INFO:root:Processing batch 31/398
INFO:root:Processing batch 32/398
INFO:root:Processing batch 33/398
INFO:root:Processing batch 34/398
INFO:root:Processing batch 35/398
INFO:root:Processing batch 36/398
INFO:root:Processing batch 37/398
INFO:root:Processing batch 38/398
INFO:root:Processing batch 39/398
INFO:root:Processing batch 40/398
INFO:root:Processing batch 41/398
INFO:root:Processing batch 42/398
INFO:root:Processing batch 43/398
INFO:root:Processing batch 44/398
INFO:root:Processing batch 45/398
INFO:root:Processing batch 46/398
INFO:root:Processing batch 47/398
INFO:root:Processing batch 48/398
INFO:root:Processing batch 49/398
INFO:root:Processing batch 50/398
INFO:root:Processing batch 51/398
INFO:root:Processing batch 52/398
INFO:root:Processing batch 53/398
INFO:root:Processing batch 54/398
INFO:root:Processing batch 55/398
INFO:root:Processing batch 56/398
INFO:root:Processing batch 57/398
INFO:root:Processing batch 58/398
INFO:root:Processing batch 59/398
INFO:root:Processing batch 60/398
INFO:root:Processing batch 61/398
INFO:root:Processing batch 62/398
INFO:root:Processing batch 63/398
INFO:root:Processing batch 64/398
INFO:root:Processing batch 65/398
INFO:root:Processing batch 66/398
INFO:root:Processing batch 67/398
INFO:root:Processing batch 68/398
INFO:root:Processing batch 69/398
INFO:root:Processing batch 70/398
INFO:root:Processing batch 71/398
INFO:root:Processing batch 72/398
INFO:root:Processing batch 73/398
INFO:root:Processing batch 74/398
INFO:root:Processing batch 75/398
INFO:root:Processing batch 76/398
INFO:root:Processing batch 77/398
INFO:root:Processing batch 78/398
INFO:root:Processing batch 79/398
INFO:root:Processing batch 80/398
INFO:root:Processing batch 81/398
INFO:root:Processing batch 82/398
INFO:root:Processing batch 83/398
INFO:root:Processing batch 84/398
INFO:root:Processing batch 85/398
INFO:root:Processing batch 86/398
INFO:root:Processing batch 87/398
INFO:root:Processing batch 88/398
INFO:root:Processing batch 89/398
INFO:root:Processing batch 90/398
INFO:root:Processing batch 91/398
INFO:root:Processing batch 92/398
INFO:root:Processing batch 93/398
INFO:root:Processing batch 94/398
INFO:root:Processing batch 95/398
INFO:root:Processing batch 96/398
INFO:root:Processing batch 97/398
INFO:root:Processing batch 98/398
INFO:root:Processing batch 99/398
INFO:root:Processing batch 100/398
INFO:root:Processing batch 101/398
INFO:root:Processing batch 102/398
INFO:root:Processing batch 103/398
INFO:root:Processing batch 104/398
INFO:root:Processing batch 105/398
INFO:root:Processing batch 106/398
INFO:root:Processing batch 107/398
INFO:root:Processing batch 108/398
INFO:root:Processing batch 109/398
INFO:root:Processing batch 110/398
INFO:root:Processing batch 111/398
INFO:root:Processing batch 112/398
INFO:root:Processing batch 113/398
INFO:root:Processing batch 114/398
INFO:root:Processing batch 115/398
INFO:root:Processing batch 116/398
INFO:root:Processing batch 117/398
INFO:root:Processing batch 118/398
INFO:root:Processing batch 119/398
INFO:root:Processing batch 120/398
INFO:root:Processing batch 121/398
INFO:root:Processing batch 122/398
INFO:root:Processing batch 123/398
INFO:root:Processing batch 124/398
INFO:root:Processing batch 125/398
INFO:root:Processing batch 126/398
INFO:root:Processing batch 127/398
INFO:root:Processing batch 128/398
INFO:root:Processing batch 129/398
INFO:root:Processing batch 130/398
INFO:root:Processing batch 131/398
INFO:root:Processing batch 132/398
INFO:root:Processing batch 133/398
INFO:root:Processing batch 134/398
INFO:root:Processing batch 135/398
INFO:root:Processing batch 136/398
INFO:root:Processing batch 137/398
INFO:root:Processing batch 138/398
INFO:root:Processing batch 139/398
INFO:root:Processing batch 140/398
INFO:root:Processing batch 141/398
INFO:root:Processing batch 142/398
INFO:root:Processing batch 143/398
INFO:root:Processing batch 144/398
INFO:root:Processing batch 145/398
INFO:root:Processing batch 146/398
INFO:root:Processing batch 147/398
INFO:root:Processing batch 148/398
INFO:root:Processing batch 149/398
INFO:root:Processing batch 150/398
INFO:root:Processing batch 151/398
INFO:root:Processing batch 152/398
INFO:root:Processing batch 153/398
INFO:root:Processing batch 154/398
INFO:root:Processing batch 155/398
INFO:root:Processing batch 156/398
INFO:root:Processing batch 157/398
INFO:root:Processing batch 158/398
INFO:root:Processing batch 159/398
INFO:root:Processing batch 160/398
INFO:root:Processing batch 161/398
INFO:root:Processing batch 162/398
INFO:root:Processing batch 163/398
INFO:root:Processing batch 164/398
INFO:root:Processing batch 165/398
INFO:root:Processing batch 166/398
INFO:root:Processing batch 167/398
INFO:root:Processing batch 168/398
INFO:root:Processing batch 169/398
INFO:root:Processing batch 170/398
INFO:root:Processing batch 171/398
INFO:root:Processing batch 172/398
INFO:root:Processing batch 173/398
INFO:root:Processing batch 174/398
INFO:root:Processing batch 175/398
INFO:root:Processing batch 176/398
INFO:root:Processing batch 177/398
INFO:root:Processing batch 178/398
INFO:root:Processing batch 179/398
INFO:root:Processing batch 180/398
INFO:root:Processing batch 181/398
INFO:root:Processing batch 182/398
INFO:root:Processing batch 183/398
INFO:root:Processing batch 184/398
INFO:root:Processing batch 185/398
INFO:root:Processing batch 186/398
INFO:root:Processing batch 187/398
INFO:root:Processing batch 188/398
INFO:root:Processing batch 189/398
INFO:root:Processing batch 190/398
INFO:root:Processing batch 191/398
INFO:root:Processing batch 192/398
INFO:root:Processing batch 193/398
INFO:root:Processing batch 194/398
INFO:root:Processing batch 195/398
INFO:root:Processing batch 196/398
INFO:root:Processing batch 197/398
INFO:root:Processing batch 198/398
INFO:root:Processing batch 199/398
INFO:root:Processing batch 200/398
INFO:root:Processing batch 201/398
INFO:root:Processing batch 202/398
INFO:root:Processing batch 203/398
INFO:root:Processing batch 204/398
INFO:root:Processing batch 205/398
INFO:root:Processing batch 206/398
INFO:root:Processing batch 207/398
INFO:root:Processing batch 208/398
INFO:root:Processing batch 209/398
INFO:root:Processing batch 210/398
INFO:root:Processing batch 211/398
INFO:root:Processing batch 212/398
INFO:root:Processing batch 213/398
INFO:root:Processing batch 214/398
INFO:root:Processing batch 215/398
INFO:root:Processing batch 216/398
INFO:root:Processing batch 217/398
INFO:root:Processing batch 218/398
INFO:root:Processing batch 219/398
INFO:root:Processing batch 220/398
INFO:root:Processing batch 221/398
INFO:root:Processing batch 222/398
INFO:root:Processing batch 223/398
INFO:root:Processing batch 224/398
INFO:root:Processing batch 225/398
INFO:root:Processing batch 226/398
INFO:root:Processing batch 227/398
INFO:root:Processing batch 228/398
INFO:root:Processing batch 229/398
INFO:root:Processing batch 230/398
INFO:root:Processing batch 231/398
INFO:root:Processing batch 232/398
INFO:root:Processing batch 233/398
INFO:root:Processing batch 234/398
INFO:root:Processing batch 235/398
INFO:root:Processing batch 236/398
INFO:root:Processing batch 237/398
INFO:root:Processing batch 238/398
INFO:root:Processing batch 239/398
INFO:root:Processing batch 240/398
INFO:root:Processing batch 241/398
INFO:root:Processing batch 242/398
INFO:root:Processing batch 243/398
INFO:root:Processing batch 244/398
INFO:root:Processing batch 245/398
INFO:root:Processing batch 246/398
INFO:root:Processing batch 247/398
INFO:root:Processing batch 248/398
INFO:root:Processing batch 249/398
INFO:root:Processing batch 250/398
INFO:root:Processing batch 251/398
INFO:root:Processing batch 252/398
INFO:root:Processing batch 253/398
INFO:root:Processing batch 254/398
INFO:root:Processing batch 255/398
INFO:root:Processing batch 256/398
INFO:root:Processing batch 257/398
INFO:root:Processing batch 258/398
INFO:root:Processing batch 259/398
INFO:root:Processing batch 260/398
INFO:root:Processing batch 261/398
INFO:root:Processing batch 262/398
INFO:root:Processing batch 263/398
INFO:root:Processing batch 264/398
INFO:root:Processing batch 265/398
INFO:root:Processing batch 266/398
INFO:root:Processing batch 267/398
INFO:root:Processing batch 268/398
INFO:root:Processing batch 269/398
INFO:root:Processing batch 270/398
INFO:root:Processing batch 271/398
INFO:root:Processing batch 272/398
INFO:root:Processing batch 273/398
INFO:root:Processing batch 274/398
INFO:root:Processing batch 275/398
INFO:root:Processing batch 276/398
INFO:root:Processing batch 277/398
INFO:root:Processing batch 278/398
INFO:root:Processing batch 279/398
INFO:root:Processing batch 280/398
INFO:root:Processing batch 281/398
INFO:root:Processing batch 282/398
INFO:root:Processing batch 283/398
INFO:root:Processing batch 284/398
INFO:root:Processing batch 285/398
INFO:root:Processing batch 286/398
INFO:root:Processing batch 287/398
INFO:root:Processing batch 288/398
INFO:root:Processing batch 289/398
INFO:root:Processing batch 290/398
INFO:root:Processing batch 291/398
INFO:root:Processing batch 292/398
INFO:root:Processing batch 293/398
INFO:root:Processing batch 294/398
INFO:root:Processing batch 295/398
INFO:root:Processing batch 296/398
INFO:root:Processing batch 297/398
INFO:root:Processing batch 298/398
INFO:root:Processing batch 299/398
INFO:root:Processing batch 300/398
INFO:root:Processing batch 301/398
INFO:root:Processing batch 302/398
INFO:root:Processing batch 303/398
INFO:root:Processing batch 304/398
INFO:root:Processing batch 305/398
INFO:root:Processing batch 306/398
INFO:root:Processing batch 307/398
INFO:root:Processing batch 308/398
INFO:root:Processing batch 309/398
INFO:root:Processing batch 310/398
INFO:root:Processing batch 311/398
INFO:root:Processing batch 312/398
INFO:root:Processing batch 313/398
INFO:root:Processing batch 314/398
INFO:root:Processing batch 315/398
INFO:root:Processing batch 316/398
INFO:root:Processing batch 317/398
INFO:root:Processing batch 318/398
INFO:root:Processing batch 319/398
INFO:root:Processing batch 320/398
INFO:root:Processing batch 321/398
INFO:root:Processing batch 322/398
INFO:root:Processing batch 323/398
INFO:root:Processing batch 324/398
INFO:root:Processing batch 325/398
INFO:root:Processing batch 326/398
INFO:root:Processing batch 327/398
INFO:root:Processing batch 328/398
INFO:root:Processing batch 329/398
INFO:root:Processing batch 330/398
INFO:root:Processing batch 331/398
INFO:root:Processing batch 332/398
INFO:root:Processing batch 333/398
INFO:root:Processing batch 334/398
INFO:root:Processing batch 335/398
INFO:root:Processing batch 336/398
INFO:root:Processing batch 337/398
INFO:root:Processing batch 338/398
INFO:root:Processing batch 339/398
INFO:root:Processing batch 340/398
INFO:root:Processing batch 341/398
INFO:root:Processing batch 342/398
INFO:root:Processing batch 343/398
INFO:root:Processing batch 344/398
INFO:root:Processing batch 345/398
INFO:root:Processing batch 346/398
INFO:root:Processing batch 347/398
INFO:root:Processing batch 348/398
INFO:root:Processing batch 349/398
INFO:root:Processing batch 350/398
INFO:root:Processing batch 351/398
INFO:root:Processing batch 352/398
INFO:root:Processing batch 353/398
INFO:root:Processing batch 354/398
INFO:root:Processing batch 355/398
INFO:root:Processing batch 356/398
INFO:root:Processing batch 357/398
INFO:root:Processing batch 358/398
INFO:root:Processing batch 359/398
INFO:root:Processing batch 360/398
INFO:root:Processing batch 361/398
INFO:root:Processing batch 362/398
INFO:root:Processing batch 363/398
INFO:root:Processing batch 364/398
INFO:root:Processing batch 365/398
INFO:root:Processing batch 366/398
INFO:root:Processing batch 367/398
INFO:root:Processing batch 368/398
INFO:root:Processing batch 369/398
INFO:root:Processing batch 370/398
INFO:root:Processing batch 371/398
INFO:root:Processing batch 372/398
INFO:root:Processing batch 373/398
INFO:root:Processing batch 374/398
INFO:root:Processing batch 375/398
INFO:root:Processing batch 376/398
INFO:root:Processing batch 377/398
INFO:root:Processing batch 378/398
INFO:root:Processing batch 379/398
INFO:root:Processing batch 380/398
INFO:root:Processing batch 381/398
INFO:root:Processing batch 382/398
INFO:root:Processing batch 383/398
INFO:root:Processing batch 384/398
INFO:root:Processing batch 385/398
INFO:root:Processing batch 386/398
INFO:root:Processing batch 387/398
INFO:root:Processing batch 388/398
INFO:root:Processing batch 389/398
INFO:root:Processing batch 390/398
INFO:root:Processing batch 391/398
INFO:root:Processing batch 392/398
INFO:root:Processing batch 393/398
INFO:root:Processing batch 394/398
INFO:root:Processing batch 395/398
INFO:root:Processing batch 396/398
INFO:root:Processing batch 397/398
INFO:root:Processing batch 398/398
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4748102128505707, 0.4196726083755493, 0.3590792119503021], 'std': [0.27919745445251465, 0.27405115962028503, 0.2634221911430359], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4748102128505707, 0.4196726083755493, 0.3590792119503021], std=[0.27919745445251465, 0.27405115962028503, 0.2634221911430359])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.09822
INFO:root:Training epoch 1, Iteration 20, Loss: 5.01527
INFO:root:Training epoch 1, Iteration 40, Loss: 4.75559
INFO:root:Training epoch 1, Iteration 60, Loss: 4.72017
INFO:root:Training epoch 1, Iteration 80, Loss: 4.48181
INFO:root:Training epoch 1, Iteration 100, Loss: 4.54629
INFO:root:Training epoch 1, Iteration 120, Loss: 4.51493
INFO:root:Training epoch 1, Iteration 140, Loss: 4.47975
INFO:root:Training epoch 1, Iteration 160, Loss: 4.42160
INFO:root:Training epoch 1, Iteration 180, Loss: 4.35302
INFO:root:Training epoch 1, Iteration 200, Loss: 4.33812
INFO:root:Training epoch 1, Iteration 220, Loss: 4.35678
INFO:root:Training epoch 1, Iteration 240, Loss: 4.30736
INFO:root:Training epoch 1, Iteration 260, Loss: 4.30868
INFO:root:Training epoch 1, Iteration 280, Loss: 4.28617
INFO:root:Training epoch 1, Iteration 300, Loss: 4.32756
INFO:root:Training epoch 1, Iteration 320, Loss: 4.15818
INFO:root:Training epoch 1, Iteration 340, Loss: 4.23715
INFO:root:Training epoch 1, Iteration 360, Loss: 4.21751
INFO:root:Training epoch 1, Iteration 380, Loss: 4.11943
INFO:root:Validation iteration 1, Loss: 4.31772
INFO:root:Validation iteration 8, Loss: 4.19080
INFO:root:Validation iteration 16, Loss: 4.07935
INFO:root:Validation iteration 24, Loss: 4.10168
INFO:root:Validation iteration 32, Loss: 3.90868
INFO:root:Validation iteration 40, Loss: 4.07638
INFO:root:Validation iteration 48, Loss: 4.08523
INFO:root:Validation iteration 56, Loss: 4.13259
INFO:root:Validation iteration 64, Loss: 4.13768
INFO:root:Validation iteration 72, Loss: 4.05885
INFO:root:Validation iteration 80, Loss: 4.09273
INFO:root:Validation iteration 88, Loss: 4.18305
INFO:root:Validation iteration 96, Loss: 3.89479
INFO:root:Validation iteration 104, Loss: 3.94595
INFO:root:Validation iteration 112, Loss: 4.13211
INFO:root:Validation iteration 120, Loss: 4.11009
INFO:root:Validation iteration 128, Loss: 3.96438
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.407
INFO:root:Validation accuracy: 0.070, Validation loss: 4.07398
INFO:root:Training epoch 2, Iteration 1, Loss: 3.90336
INFO:root:Training epoch 2, Iteration 20, Loss: 3.91380
INFO:root:Training epoch 2, Iteration 40, Loss: 3.89043
INFO:root:Training epoch 2, Iteration 60, Loss: 3.91488
INFO:root:Training epoch 2, Iteration 80, Loss: 4.00372
INFO:root:Training epoch 2, Iteration 100, Loss: 3.87812
INFO:root:Training epoch 2, Iteration 120, Loss: 4.03281
INFO:root:Training epoch 2, Iteration 140, Loss: 4.05142
INFO:root:Training epoch 2, Iteration 160, Loss: 4.04688
INFO:root:Training epoch 2, Iteration 180, Loss: 3.88460
INFO:root:Training epoch 2, Iteration 200, Loss: 3.91250
INFO:root:Training epoch 2, Iteration 220, Loss: 3.88807
INFO:root:Training epoch 2, Iteration 240, Loss: 3.81369
INFO:root:Training epoch 2, Iteration 260, Loss: 4.03551
INFO:root:Training epoch 2, Iteration 280, Loss: 3.84012
INFO:root:Training epoch 2, Iteration 300, Loss: 3.93898
INFO:root:Training epoch 2, Iteration 320, Loss: 3.85785
INFO:root:Training epoch 2, Iteration 340, Loss: 3.71540
INFO:root:Training epoch 2, Iteration 360, Loss: 3.84428
INFO:root:Training epoch 2, Iteration 380, Loss: 3.92135
INFO:root:Validation iteration 1, Loss: 4.24949
INFO:root:Validation iteration 8, Loss: 3.86813
INFO:root:Validation iteration 16, Loss: 3.75922
INFO:root:Validation iteration 24, Loss: 3.83998
INFO:root:Validation iteration 32, Loss: 3.75764
INFO:root:Validation iteration 40, Loss: 3.76291
INFO:root:Validation iteration 48, Loss: 3.78806
INFO:root:Validation iteration 56, Loss: 3.85334
INFO:root:Validation iteration 64, Loss: 3.81818
INFO:root:Validation iteration 72, Loss: 3.67625
INFO:root:Validation iteration 80, Loss: 3.81119
INFO:root:Validation iteration 88, Loss: 3.93923
INFO:root:Validation iteration 96, Loss: 3.61587
INFO:root:Validation iteration 104, Loss: 3.67526
INFO:root:Validation iteration 112, Loss: 3.77402
INFO:root:Validation iteration 120, Loss: 3.85194
INFO:root:Validation iteration 128, Loss: 3.73748
INFO:root:End of Epoch 2
INFO:root:Training loss: 3.909
INFO:root:Validation accuracy: 0.113, Validation loss: 3.78827
INFO:root:Best validation accuracy: 0.113 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.85400
INFO:root:Validation iteration 8, Loss: 3.96134
INFO:root:Validation iteration 16, Loss: 3.87167
INFO:root:Validation iteration 24, Loss: 3.87756
INFO:root:Validation iteration 32, Loss: 3.70209
INFO:root:Validation iteration 40, Loss: 3.89833
INFO:root:Validation iteration 48, Loss: 3.79679
INFO:root:Validation iteration 56, Loss: 3.62399
INFO:root:Validation iteration 64, Loss: 3.60506
INFO:root:Validation iteration 72, Loss: 3.78434
INFO:root:Validation iteration 80, Loss: 3.66333
INFO:root:Validation iteration 88, Loss: 3.84803
INFO:root:Validation iteration 96, Loss: 3.69771
INFO:root:Validation iteration 104, Loss: 3.84966
INFO:root:Validation iteration 112, Loss: 3.86193
INFO:root:Validation iteration 120, Loss: 3.80296
INFO:root:Validation iteration 128, Loss: 3.85034
Test accuracy: 0.140, Test loss: 3.80044
INFO:root:Saving results...
INFO:root:Done!
"""

string15 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=32, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=20, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='weighted_cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/398
INFO:root:Processing batch 2/398
INFO:root:Processing batch 3/398
INFO:root:Processing batch 4/398
INFO:root:Processing batch 5/398
INFO:root:Processing batch 6/398
INFO:root:Processing batch 7/398
INFO:root:Processing batch 8/398
INFO:root:Processing batch 9/398
INFO:root:Processing batch 10/398
INFO:root:Processing batch 11/398
INFO:root:Processing batch 12/398
INFO:root:Processing batch 13/398
INFO:root:Processing batch 14/398
INFO:root:Processing batch 15/398
INFO:root:Processing batch 16/398
INFO:root:Processing batch 17/398
INFO:root:Processing batch 18/398
INFO:root:Processing batch 19/398
INFO:root:Processing batch 20/398
INFO:root:Processing batch 21/398
INFO:root:Processing batch 22/398
INFO:root:Processing batch 23/398
INFO:root:Processing batch 24/398
INFO:root:Processing batch 25/398
INFO:root:Processing batch 26/398
INFO:root:Processing batch 27/398
INFO:root:Processing batch 28/398
INFO:root:Processing batch 29/398
INFO:root:Processing batch 30/398
INFO:root:Processing batch 31/398
INFO:root:Processing batch 32/398
INFO:root:Processing batch 33/398
INFO:root:Processing batch 34/398
INFO:root:Processing batch 35/398
INFO:root:Processing batch 36/398
INFO:root:Processing batch 37/398
INFO:root:Processing batch 38/398
INFO:root:Processing batch 39/398
INFO:root:Processing batch 40/398
INFO:root:Processing batch 41/398
INFO:root:Processing batch 42/398
INFO:root:Processing batch 43/398
INFO:root:Processing batch 44/398
INFO:root:Processing batch 45/398
INFO:root:Processing batch 46/398
INFO:root:Processing batch 47/398
INFO:root:Processing batch 48/398
INFO:root:Processing batch 49/398
INFO:root:Processing batch 50/398
INFO:root:Processing batch 51/398
INFO:root:Processing batch 52/398
INFO:root:Processing batch 53/398
INFO:root:Processing batch 54/398
INFO:root:Processing batch 55/398
INFO:root:Processing batch 56/398
INFO:root:Processing batch 57/398
INFO:root:Processing batch 58/398
INFO:root:Processing batch 59/398
INFO:root:Processing batch 60/398
INFO:root:Processing batch 61/398
INFO:root:Processing batch 62/398
INFO:root:Processing batch 63/398
INFO:root:Processing batch 64/398
INFO:root:Processing batch 65/398
INFO:root:Processing batch 66/398
INFO:root:Processing batch 67/398
INFO:root:Processing batch 68/398
INFO:root:Processing batch 69/398
INFO:root:Processing batch 70/398
INFO:root:Processing batch 71/398
INFO:root:Processing batch 72/398
INFO:root:Processing batch 73/398
INFO:root:Processing batch 74/398
INFO:root:Processing batch 75/398
INFO:root:Processing batch 76/398
INFO:root:Processing batch 77/398
INFO:root:Processing batch 78/398
INFO:root:Processing batch 79/398
INFO:root:Processing batch 80/398
INFO:root:Processing batch 81/398
INFO:root:Processing batch 82/398
INFO:root:Processing batch 83/398
INFO:root:Processing batch 84/398
INFO:root:Processing batch 85/398
INFO:root:Processing batch 86/398
INFO:root:Processing batch 87/398
INFO:root:Processing batch 88/398
INFO:root:Processing batch 89/398
INFO:root:Processing batch 90/398
INFO:root:Processing batch 91/398
INFO:root:Processing batch 92/398
INFO:root:Processing batch 93/398
INFO:root:Processing batch 94/398
INFO:root:Processing batch 95/398
INFO:root:Processing batch 96/398
INFO:root:Processing batch 97/398
INFO:root:Processing batch 98/398
INFO:root:Processing batch 99/398
INFO:root:Processing batch 100/398
INFO:root:Processing batch 101/398
INFO:root:Processing batch 102/398
INFO:root:Processing batch 103/398
INFO:root:Processing batch 104/398
INFO:root:Processing batch 105/398
INFO:root:Processing batch 106/398
INFO:root:Processing batch 107/398
INFO:root:Processing batch 108/398
INFO:root:Processing batch 109/398
INFO:root:Processing batch 110/398
INFO:root:Processing batch 111/398
INFO:root:Processing batch 112/398
INFO:root:Processing batch 113/398
INFO:root:Processing batch 114/398
INFO:root:Processing batch 115/398
INFO:root:Processing batch 116/398
INFO:root:Processing batch 117/398
INFO:root:Processing batch 118/398
INFO:root:Processing batch 119/398
INFO:root:Processing batch 120/398
INFO:root:Processing batch 121/398
INFO:root:Processing batch 122/398
INFO:root:Processing batch 123/398
INFO:root:Processing batch 124/398
INFO:root:Processing batch 125/398
INFO:root:Processing batch 126/398
INFO:root:Processing batch 127/398
INFO:root:Processing batch 128/398
INFO:root:Processing batch 129/398
INFO:root:Processing batch 130/398
INFO:root:Processing batch 131/398
INFO:root:Processing batch 132/398
INFO:root:Processing batch 133/398
INFO:root:Processing batch 134/398
INFO:root:Processing batch 135/398
INFO:root:Processing batch 136/398
INFO:root:Processing batch 137/398
INFO:root:Processing batch 138/398
INFO:root:Processing batch 139/398
INFO:root:Processing batch 140/398
INFO:root:Processing batch 141/398
INFO:root:Processing batch 142/398
INFO:root:Processing batch 143/398
INFO:root:Processing batch 144/398
INFO:root:Processing batch 145/398
INFO:root:Processing batch 146/398
INFO:root:Processing batch 147/398
INFO:root:Processing batch 148/398
INFO:root:Processing batch 149/398
INFO:root:Processing batch 150/398
INFO:root:Processing batch 151/398
INFO:root:Processing batch 152/398
INFO:root:Processing batch 153/398
INFO:root:Processing batch 154/398
INFO:root:Processing batch 155/398
INFO:root:Processing batch 156/398
INFO:root:Processing batch 157/398
INFO:root:Processing batch 158/398
INFO:root:Processing batch 159/398
INFO:root:Processing batch 160/398
INFO:root:Processing batch 161/398
INFO:root:Processing batch 162/398
INFO:root:Processing batch 163/398
INFO:root:Processing batch 164/398
INFO:root:Processing batch 165/398
INFO:root:Processing batch 166/398
INFO:root:Processing batch 167/398
INFO:root:Processing batch 168/398
INFO:root:Processing batch 169/398
INFO:root:Processing batch 170/398
INFO:root:Processing batch 171/398
INFO:root:Processing batch 172/398
INFO:root:Processing batch 173/398
INFO:root:Processing batch 174/398
INFO:root:Processing batch 175/398
INFO:root:Processing batch 176/398
INFO:root:Processing batch 177/398
INFO:root:Processing batch 178/398
INFO:root:Processing batch 179/398
INFO:root:Processing batch 180/398
INFO:root:Processing batch 181/398
INFO:root:Processing batch 182/398
INFO:root:Processing batch 183/398
INFO:root:Processing batch 184/398
INFO:root:Processing batch 185/398
INFO:root:Processing batch 186/398
INFO:root:Processing batch 187/398
INFO:root:Processing batch 188/398
INFO:root:Processing batch 189/398
INFO:root:Processing batch 190/398
INFO:root:Processing batch 191/398
INFO:root:Processing batch 192/398
INFO:root:Processing batch 193/398
INFO:root:Processing batch 194/398
INFO:root:Processing batch 195/398
INFO:root:Processing batch 196/398
INFO:root:Processing batch 197/398
INFO:root:Processing batch 198/398
INFO:root:Processing batch 199/398
INFO:root:Processing batch 200/398
INFO:root:Processing batch 201/398
INFO:root:Processing batch 202/398
INFO:root:Processing batch 203/398
INFO:root:Processing batch 204/398
INFO:root:Processing batch 205/398
INFO:root:Processing batch 206/398
INFO:root:Processing batch 207/398
INFO:root:Processing batch 208/398
INFO:root:Processing batch 209/398
INFO:root:Processing batch 210/398
INFO:root:Processing batch 211/398
INFO:root:Processing batch 212/398
INFO:root:Processing batch 213/398
INFO:root:Processing batch 214/398
INFO:root:Processing batch 215/398
INFO:root:Processing batch 216/398
INFO:root:Processing batch 217/398
INFO:root:Processing batch 218/398
INFO:root:Processing batch 219/398
INFO:root:Processing batch 220/398
INFO:root:Processing batch 221/398
INFO:root:Processing batch 222/398
INFO:root:Processing batch 223/398
INFO:root:Processing batch 224/398
INFO:root:Processing batch 225/398
INFO:root:Processing batch 226/398
INFO:root:Processing batch 227/398
INFO:root:Processing batch 228/398
INFO:root:Processing batch 229/398
INFO:root:Processing batch 230/398
INFO:root:Processing batch 231/398
INFO:root:Processing batch 232/398
INFO:root:Processing batch 233/398
INFO:root:Processing batch 234/398
INFO:root:Processing batch 235/398
INFO:root:Processing batch 236/398
INFO:root:Processing batch 237/398
INFO:root:Processing batch 238/398
INFO:root:Processing batch 239/398
INFO:root:Processing batch 240/398
INFO:root:Processing batch 241/398
INFO:root:Processing batch 242/398
INFO:root:Processing batch 243/398
INFO:root:Processing batch 244/398
INFO:root:Processing batch 245/398
INFO:root:Processing batch 246/398
INFO:root:Processing batch 247/398
INFO:root:Processing batch 248/398
INFO:root:Processing batch 249/398
INFO:root:Processing batch 250/398
INFO:root:Processing batch 251/398
INFO:root:Processing batch 252/398
INFO:root:Processing batch 253/398
INFO:root:Processing batch 254/398
INFO:root:Processing batch 255/398
INFO:root:Processing batch 256/398
INFO:root:Processing batch 257/398
INFO:root:Processing batch 258/398
INFO:root:Processing batch 259/398
INFO:root:Processing batch 260/398
INFO:root:Processing batch 261/398
INFO:root:Processing batch 262/398
INFO:root:Processing batch 263/398
INFO:root:Processing batch 264/398
INFO:root:Processing batch 265/398
INFO:root:Processing batch 266/398
INFO:root:Processing batch 267/398
INFO:root:Processing batch 268/398
INFO:root:Processing batch 269/398
INFO:root:Processing batch 270/398
INFO:root:Processing batch 271/398
INFO:root:Processing batch 272/398
INFO:root:Processing batch 273/398
INFO:root:Processing batch 274/398
INFO:root:Processing batch 275/398
INFO:root:Processing batch 276/398
INFO:root:Processing batch 277/398
INFO:root:Processing batch 278/398
INFO:root:Processing batch 279/398
INFO:root:Processing batch 280/398
INFO:root:Processing batch 281/398
INFO:root:Processing batch 282/398
INFO:root:Processing batch 283/398
INFO:root:Processing batch 284/398
INFO:root:Processing batch 285/398
INFO:root:Processing batch 286/398
INFO:root:Processing batch 287/398
INFO:root:Processing batch 288/398
INFO:root:Processing batch 289/398
INFO:root:Processing batch 290/398
INFO:root:Processing batch 291/398
INFO:root:Processing batch 292/398
INFO:root:Processing batch 293/398
INFO:root:Processing batch 294/398
INFO:root:Processing batch 295/398
INFO:root:Processing batch 296/398
INFO:root:Processing batch 297/398
INFO:root:Processing batch 298/398
INFO:root:Processing batch 299/398
INFO:root:Processing batch 300/398
INFO:root:Processing batch 301/398
INFO:root:Processing batch 302/398
INFO:root:Processing batch 303/398
INFO:root:Processing batch 304/398
INFO:root:Processing batch 305/398
INFO:root:Processing batch 306/398
INFO:root:Processing batch 307/398
INFO:root:Processing batch 308/398
INFO:root:Processing batch 309/398
INFO:root:Processing batch 310/398
INFO:root:Processing batch 311/398
INFO:root:Processing batch 312/398
INFO:root:Processing batch 313/398
INFO:root:Processing batch 314/398
INFO:root:Processing batch 315/398
INFO:root:Processing batch 316/398
INFO:root:Processing batch 317/398
INFO:root:Processing batch 318/398
INFO:root:Processing batch 319/398
INFO:root:Processing batch 320/398
INFO:root:Processing batch 321/398
INFO:root:Processing batch 322/398
INFO:root:Processing batch 323/398
INFO:root:Processing batch 324/398
INFO:root:Processing batch 325/398
INFO:root:Processing batch 326/398
INFO:root:Processing batch 327/398
INFO:root:Processing batch 328/398
INFO:root:Processing batch 329/398
INFO:root:Processing batch 330/398
INFO:root:Processing batch 331/398
INFO:root:Processing batch 332/398
INFO:root:Processing batch 333/398
INFO:root:Processing batch 334/398
INFO:root:Processing batch 335/398
INFO:root:Processing batch 336/398
INFO:root:Processing batch 337/398
INFO:root:Processing batch 338/398
INFO:root:Processing batch 339/398
INFO:root:Processing batch 340/398
INFO:root:Processing batch 341/398
INFO:root:Processing batch 342/398
INFO:root:Processing batch 343/398
INFO:root:Processing batch 344/398
INFO:root:Processing batch 345/398
INFO:root:Processing batch 346/398
INFO:root:Processing batch 347/398
INFO:root:Processing batch 348/398
INFO:root:Processing batch 349/398
INFO:root:Processing batch 350/398
INFO:root:Processing batch 351/398
INFO:root:Processing batch 352/398
INFO:root:Processing batch 353/398
INFO:root:Processing batch 354/398
INFO:root:Processing batch 355/398
INFO:root:Processing batch 356/398
INFO:root:Processing batch 357/398
INFO:root:Processing batch 358/398
INFO:root:Processing batch 359/398
INFO:root:Processing batch 360/398
INFO:root:Processing batch 361/398
INFO:root:Processing batch 362/398
INFO:root:Processing batch 363/398
INFO:root:Processing batch 364/398
INFO:root:Processing batch 365/398
INFO:root:Processing batch 366/398
INFO:root:Processing batch 367/398
INFO:root:Processing batch 368/398
INFO:root:Processing batch 369/398
INFO:root:Processing batch 370/398
INFO:root:Processing batch 371/398
INFO:root:Processing batch 372/398
INFO:root:Processing batch 373/398
INFO:root:Processing batch 374/398
INFO:root:Processing batch 375/398
INFO:root:Processing batch 376/398
INFO:root:Processing batch 377/398
INFO:root:Processing batch 378/398
INFO:root:Processing batch 379/398
INFO:root:Processing batch 380/398
INFO:root:Processing batch 381/398
INFO:root:Processing batch 382/398
INFO:root:Processing batch 383/398
INFO:root:Processing batch 384/398
INFO:root:Processing batch 385/398
INFO:root:Processing batch 386/398
INFO:root:Processing batch 387/398
INFO:root:Processing batch 388/398
INFO:root:Processing batch 389/398
INFO:root:Processing batch 390/398
INFO:root:Processing batch 391/398
INFO:root:Processing batch 392/398
INFO:root:Processing batch 393/398
INFO:root:Processing batch 394/398
INFO:root:Processing batch 395/398
INFO:root:Processing batch 396/398
INFO:root:Processing batch 397/398
INFO:root:Processing batch 398/398
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4748102128505707, 0.4196726083755493, 0.3590792119503021], 'std': [0.27919745445251465, 0.27405115962028503, 0.2634221911430359], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4748102128505707, 0.4196726083755493, 0.3590792119503021], std=[0.27919745445251465, 0.27405115962028503, 0.2634221911430359])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.05027
INFO:root:Training epoch 1, Iteration 20, Loss: 4.99013
INFO:root:Training epoch 1, Iteration 40, Loss: 4.72979
INFO:root:Training epoch 1, Iteration 60, Loss: 4.65524
INFO:root:Training epoch 1, Iteration 80, Loss: 4.66744
INFO:root:Training epoch 1, Iteration 100, Loss: 4.57009
INFO:root:Training epoch 1, Iteration 120, Loss: 4.45415
INFO:root:Training epoch 1, Iteration 140, Loss: 4.52468
INFO:root:Training epoch 1, Iteration 160, Loss: 4.36170
INFO:root:Training epoch 1, Iteration 180, Loss: 4.41588
INFO:root:Training epoch 1, Iteration 200, Loss: 4.33173
INFO:root:Training epoch 1, Iteration 220, Loss: 4.48313
INFO:root:Training epoch 1, Iteration 240, Loss: 4.23910
INFO:root:Training epoch 1, Iteration 260, Loss: 4.26687
INFO:root:Training epoch 1, Iteration 280, Loss: 4.18602
INFO:root:Training epoch 1, Iteration 300, Loss: 4.16265
INFO:root:Training epoch 1, Iteration 320, Loss: 4.16884
INFO:root:Training epoch 1, Iteration 340, Loss: 4.14383
INFO:root:Training epoch 1, Iteration 360, Loss: 4.19785
INFO:root:Training epoch 1, Iteration 380, Loss: 4.13485
INFO:root:Validation iteration 1, Loss: 4.64822
INFO:root:Validation iteration 8, Loss: 4.18491
INFO:root:Validation iteration 16, Loss: 4.08472
INFO:root:Validation iteration 24, Loss: 4.11296
INFO:root:Validation iteration 32, Loss: 4.08346
INFO:root:Validation iteration 40, Loss: 4.12780
INFO:root:Validation iteration 48, Loss: 4.19782
INFO:root:Validation iteration 56, Loss: 4.14545
INFO:root:Validation iteration 64, Loss: 4.21188
INFO:root:Validation iteration 72, Loss: 4.05574
INFO:root:Validation iteration 80, Loss: 4.24177
INFO:root:Validation iteration 88, Loss: 4.36869
INFO:root:Validation iteration 96, Loss: 3.94533
INFO:root:Validation iteration 104, Loss: 4.09868
INFO:root:Validation iteration 112, Loss: 4.26422
INFO:root:Validation iteration 120, Loss: 4.34025
INFO:root:Validation iteration 128, Loss: 4.23460
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.395
INFO:root:Validation accuracy: 0.064, Validation loss: 4.17228
INFO:root:Training epoch 2, Iteration 1, Loss: 3.72670
INFO:root:Training epoch 2, Iteration 20, Loss: 3.88939
INFO:root:Training epoch 2, Iteration 40, Loss: 4.04462
INFO:root:Training epoch 2, Iteration 60, Loss: 4.07276
INFO:root:Training epoch 2, Iteration 80, Loss: 3.83918
INFO:root:Training epoch 2, Iteration 100, Loss: 3.94223
INFO:root:Training epoch 2, Iteration 120, Loss: 3.95803
INFO:root:Training epoch 2, Iteration 140, Loss: 3.95908
INFO:root:Training epoch 2, Iteration 160, Loss: 4.01437
INFO:root:Training epoch 2, Iteration 180, Loss: 3.92014
INFO:root:Training epoch 2, Iteration 200, Loss: 3.94183
INFO:root:Training epoch 2, Iteration 220, Loss: 3.88777
INFO:root:Training epoch 2, Iteration 240, Loss: 3.95753
INFO:root:Training epoch 2, Iteration 260, Loss: 3.91245
INFO:root:Training epoch 2, Iteration 280, Loss: 3.95295
INFO:root:Training epoch 2, Iteration 300, Loss: 3.74986
INFO:root:Training epoch 2, Iteration 320, Loss: 3.88949
INFO:root:Training epoch 2, Iteration 340, Loss: 3.81783
INFO:root:Training epoch 2, Iteration 360, Loss: 3.87196
INFO:root:Training epoch 2, Iteration 380, Loss: 3.78454
INFO:root:Validation iteration 1, Loss: 4.28955
INFO:root:Validation iteration 8, Loss: 3.95940
INFO:root:Validation iteration 16, Loss: 3.85352
INFO:root:Validation iteration 24, Loss: 3.76075
INFO:root:Validation iteration 32, Loss: 3.75533
INFO:root:Validation iteration 40, Loss: 3.79209
INFO:root:Validation iteration 48, Loss: 3.79090
INFO:root:Validation iteration 56, Loss: 3.91969
INFO:root:Validation iteration 64, Loss: 3.80718
INFO:root:Validation iteration 72, Loss: 3.77200
INFO:root:Validation iteration 80, Loss: 3.80798
INFO:root:Validation iteration 88, Loss: 4.03126
INFO:root:Validation iteration 96, Loss: 3.60032
INFO:root:Validation iteration 104, Loss: 3.68573
INFO:root:Validation iteration 112, Loss: 3.87361
INFO:root:Validation iteration 120, Loss: 3.70666
INFO:root:Validation iteration 128, Loss: 3.73720
INFO:root:End of Epoch 2
INFO:root:Training loss: 3.916
INFO:root:Validation accuracy: 0.107, Validation loss: 3.80878
INFO:root:Best validation accuracy: 0.107 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 4.10525
INFO:root:Validation iteration 8, Loss: 4.05508
INFO:root:Validation iteration 16, Loss: 3.84667
INFO:root:Validation iteration 24, Loss: 3.99725
INFO:root:Validation iteration 32, Loss: 3.75492
INFO:root:Validation iteration 40, Loss: 3.91730
INFO:root:Validation iteration 48, Loss: 3.69277
INFO:root:Validation iteration 56, Loss: 3.72257
INFO:root:Validation iteration 64, Loss: 3.58742
INFO:root:Validation iteration 72, Loss: 3.75473
INFO:root:Validation iteration 80, Loss: 3.65481
INFO:root:Validation iteration 88, Loss: 3.89257
INFO:root:Validation iteration 96, Loss: 3.73949
INFO:root:Validation iteration 104, Loss: 3.66005
INFO:root:Validation iteration 112, Loss: 3.91924
INFO:root:Validation iteration 120, Loss: 3.80704
INFO:root:Validation iteration 128, Loss: 3.89167
Test accuracy: 0.136, Test loss: 3.81357
INFO:root:Saving results...
INFO:root:Done!
"""

string16 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='weighted_cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4748101532459259, 0.41967248916625977, 0.35907915234565735], 'std': [0.279197633266449, 0.27405133843421936, 0.2634223997592926], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4748101532459259, 0.41967248916625977, 0.35907915234565735], std=[0.279197633266449, 0.27405133843421936, 0.2634223997592926])']}}}
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 152MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.09988
INFO:root:Training epoch 1, Iteration 30, Loss: 5.05296
INFO:root:Training epoch 1, Iteration 60, Loss: 4.83972
INFO:root:Training epoch 1, Iteration 90, Loss: 4.81060
INFO:root:Training epoch 1, Iteration 120, Loss: 4.67637
INFO:root:Training epoch 1, Iteration 150, Loss: 4.75250
INFO:root:Training epoch 1, Iteration 180, Loss: 4.59111
INFO:root:Training epoch 1, Iteration 210, Loss: 4.51944
INFO:root:Training epoch 1, Iteration 240, Loss: 4.54903
INFO:root:Training epoch 1, Iteration 270, Loss: 4.36588
INFO:root:Training epoch 1, Iteration 300, Loss: 4.46189
INFO:root:Training epoch 1, Iteration 330, Loss: 4.55257
INFO:root:Training epoch 1, Iteration 360, Loss: 4.35590
INFO:root:Training epoch 1, Iteration 390, Loss: 4.36010
INFO:root:Training epoch 1, Iteration 420, Loss: 4.26120
INFO:root:Training epoch 1, Iteration 450, Loss: 4.34338
INFO:root:Training epoch 1, Iteration 480, Loss: 4.35422
INFO:root:Training epoch 1, Iteration 510, Loss: 4.30407
INFO:root:Training epoch 1, Iteration 540, Loss: 4.24374
INFO:root:Training epoch 1, Iteration 570, Loss: 4.36395
INFO:root:Training epoch 1, Iteration 600, Loss: 4.31464
INFO:root:Training epoch 1, Iteration 630, Loss: 4.17379
INFO:root:Training epoch 1, Iteration 660, Loss: 4.36650
INFO:root:Training epoch 1, Iteration 690, Loss: 4.12575
INFO:root:Training epoch 1, Iteration 720, Loss: 4.11508
INFO:root:Training epoch 1, Iteration 750, Loss: 4.18432
INFO:root:Training epoch 1, Iteration 780, Loss: 4.24625
INFO:root:Validation iteration 1, Loss: 4.67741
INFO:root:Validation iteration 10, Loss: 4.31131
INFO:root:Validation iteration 20, Loss: 4.25474
INFO:root:Validation iteration 30, Loss: 4.30601
INFO:root:Validation iteration 40, Loss: 4.30789
INFO:root:Validation iteration 50, Loss: 4.31090
INFO:root:Validation iteration 60, Loss: 4.20984
INFO:root:Validation iteration 70, Loss: 4.09058
INFO:root:Validation iteration 80, Loss: 4.10067
INFO:root:Validation iteration 90, Loss: 3.79413
INFO:root:Validation iteration 100, Loss: 4.29582
INFO:root:Validation iteration 110, Loss: 4.55165
INFO:root:Validation iteration 120, Loss: 4.11019
INFO:root:Validation iteration 130, Loss: 4.18282
INFO:root:Validation iteration 140, Loss: 4.36610
INFO:root:Validation iteration 150, Loss: 4.26933
INFO:root:Validation iteration 160, Loss: 4.27511
INFO:root:Validation iteration 170, Loss: 4.50544
INFO:root:Validation iteration 180, Loss: 4.38499
INFO:root:Validation iteration 190, Loss: 4.00436
INFO:root:Validation iteration 200, Loss: 4.18011
INFO:root:Validation iteration 210, Loss: 3.98552
INFO:root:Validation iteration 220, Loss: 4.39696
INFO:root:Validation iteration 230, Loss: 4.46073
INFO:root:Validation iteration 240, Loss: 4.14699
INFO:root:Validation iteration 250, Loss: 4.08353
INFO:root:Validation iteration 260, Loss: 4.22871
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.430
INFO:root:Validation accuracy: 0.066, Validation loss: 4.23469
INFO:root:Training epoch 2, Iteration 1, Loss: 3.31209
INFO:root:Training epoch 2, Iteration 30, Loss: 4.07828
INFO:root:Training epoch 2, Iteration 60, Loss: 4.11526
INFO:root:Training epoch 2, Iteration 90, Loss: 3.99370
INFO:root:Training epoch 2, Iteration 120, Loss: 4.09207
INFO:root:Training epoch 2, Iteration 150, Loss: 4.03196
INFO:root:Training epoch 2, Iteration 180, Loss: 4.11168
INFO:root:Training epoch 2, Iteration 210, Loss: 4.15285
INFO:root:Training epoch 2, Iteration 240, Loss: 4.14708
INFO:root:Training epoch 2, Iteration 270, Loss: 4.15163
INFO:root:Training epoch 2, Iteration 300, Loss: 3.97793
INFO:root:Training epoch 2, Iteration 330, Loss: 4.20356
INFO:root:Training epoch 2, Iteration 360, Loss: 3.95044
INFO:root:Training epoch 2, Iteration 390, Loss: 4.14577
INFO:root:Training epoch 2, Iteration 420, Loss: 3.94943
INFO:root:Training epoch 2, Iteration 450, Loss: 3.89981
INFO:root:Training epoch 2, Iteration 480, Loss: 4.05254
INFO:root:Training epoch 2, Iteration 510, Loss: 4.02686
INFO:root:Training epoch 2, Iteration 540, Loss: 4.07042
INFO:root:Training epoch 2, Iteration 570, Loss: 3.89263
INFO:root:Training epoch 2, Iteration 600, Loss: 3.98951
INFO:root:Training epoch 2, Iteration 630, Loss: 3.89507
INFO:root:Training epoch 2, Iteration 660, Loss: 3.91904
INFO:root:Training epoch 2, Iteration 690, Loss: 3.97581
INFO:root:Training epoch 2, Iteration 720, Loss: 3.92808
INFO:root:Training epoch 2, Iteration 750, Loss: 4.11238
INFO:root:Training epoch 2, Iteration 780, Loss: 3.89786
INFO:root:Validation iteration 1, Loss: 4.68898
INFO:root:Validation iteration 10, Loss: 4.20976
INFO:root:Validation iteration 20, Loss: 3.63249
INFO:root:Validation iteration 30, Loss: 3.98780
INFO:root:Validation iteration 40, Loss: 3.94958
INFO:root:Validation iteration 50, Loss: 3.78717
INFO:root:Validation iteration 60, Loss: 3.78286
INFO:root:Validation iteration 70, Loss: 3.78170
INFO:root:Validation iteration 80, Loss: 3.83753
INFO:root:Validation iteration 90, Loss: 3.64167
INFO:root:Validation iteration 100, Loss: 3.97365
INFO:root:Validation iteration 110, Loss: 4.06975
INFO:root:Validation iteration 120, Loss: 3.88663
INFO:root:Validation iteration 130, Loss: 3.80646
INFO:root:Validation iteration 140, Loss: 3.89025
INFO:root:Validation iteration 150, Loss: 4.05921
INFO:root:Validation iteration 160, Loss: 3.90233
INFO:root:Validation iteration 170, Loss: 3.89467
INFO:root:Validation iteration 180, Loss: 4.01627
INFO:root:Validation iteration 190, Loss: 3.74299
INFO:root:Validation iteration 200, Loss: 3.77218
INFO:root:Validation iteration 210, Loss: 3.73445
INFO:root:Validation iteration 220, Loss: 3.83894
INFO:root:Validation iteration 230, Loss: 3.91145
INFO:root:Validation iteration 240, Loss: 4.00912
INFO:root:Validation iteration 250, Loss: 3.79953
INFO:root:Validation iteration 260, Loss: 3.95238
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.028
INFO:root:Validation accuracy: 0.103, Validation loss: 3.87491
INFO:root:Best validation accuracy: 0.103 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.44114
INFO:root:Validation iteration 10, Loss: 4.02473
INFO:root:Validation iteration 20, Loss: 4.16149
INFO:root:Validation iteration 30, Loss: 4.31584
INFO:root:Validation iteration 40, Loss: 3.96477
INFO:root:Validation iteration 50, Loss: 3.92488
INFO:root:Validation iteration 60, Loss: 3.75287
INFO:root:Validation iteration 70, Loss: 3.81675
INFO:root:Validation iteration 80, Loss: 4.11973
INFO:root:Validation iteration 90, Loss: 3.72105
INFO:root:Validation iteration 100, Loss: 3.89648
INFO:root:Validation iteration 110, Loss: 3.87926
INFO:root:Validation iteration 120, Loss: 3.72733
INFO:root:Validation iteration 130, Loss: 3.73981
INFO:root:Validation iteration 140, Loss: 4.01863
INFO:root:Validation iteration 150, Loss: 3.87120
INFO:root:Validation iteration 160, Loss: 3.73046
INFO:root:Validation iteration 170, Loss: 3.76699
INFO:root:Validation iteration 180, Loss: 4.03701
INFO:root:Validation iteration 190, Loss: 3.82530
INFO:root:Validation iteration 200, Loss: 3.93885
INFO:root:Validation iteration 210, Loss: 3.78239
INFO:root:Validation iteration 220, Loss: 4.04300
INFO:root:Validation iteration 230, Loss: 3.78148
INFO:root:Validation iteration 240, Loss: 3.91673
INFO:root:Validation iteration 250, Loss: 3.84963
INFO:root:Validation iteration 260, Loss: 3.91379
Test accuracy: 0.133, Test loss: 3.90933
INFO:root:Saving results...
INFO:root:Done!"""

string17 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=16, train_split_size=0.75), 'train': TrainConfig(num_epochs=2, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='weighted_cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=True, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/796
INFO:root:Processing batch 2/796
INFO:root:Processing batch 3/796
INFO:root:Processing batch 4/796
INFO:root:Processing batch 5/796
INFO:root:Processing batch 6/796
INFO:root:Processing batch 7/796
INFO:root:Processing batch 8/796
INFO:root:Processing batch 9/796
INFO:root:Processing batch 10/796
INFO:root:Processing batch 11/796
INFO:root:Processing batch 12/796
INFO:root:Processing batch 13/796
INFO:root:Processing batch 14/796
INFO:root:Processing batch 15/796
INFO:root:Processing batch 16/796
INFO:root:Processing batch 17/796
INFO:root:Processing batch 18/796
INFO:root:Processing batch 19/796
INFO:root:Processing batch 20/796
INFO:root:Processing batch 21/796
INFO:root:Processing batch 22/796
INFO:root:Processing batch 23/796
INFO:root:Processing batch 24/796
INFO:root:Processing batch 25/796
INFO:root:Processing batch 26/796
INFO:root:Processing batch 27/796
INFO:root:Processing batch 28/796
INFO:root:Processing batch 29/796
INFO:root:Processing batch 30/796
INFO:root:Processing batch 31/796
INFO:root:Processing batch 32/796
INFO:root:Processing batch 33/796
INFO:root:Processing batch 34/796
INFO:root:Processing batch 35/796
INFO:root:Processing batch 36/796
INFO:root:Processing batch 37/796
INFO:root:Processing batch 38/796
INFO:root:Processing batch 39/796
INFO:root:Processing batch 40/796
INFO:root:Processing batch 41/796
INFO:root:Processing batch 42/796
INFO:root:Processing batch 43/796
INFO:root:Processing batch 44/796
INFO:root:Processing batch 45/796
INFO:root:Processing batch 46/796
INFO:root:Processing batch 47/796
INFO:root:Processing batch 48/796
INFO:root:Processing batch 49/796
INFO:root:Processing batch 50/796
INFO:root:Processing batch 51/796
INFO:root:Processing batch 52/796
INFO:root:Processing batch 53/796
INFO:root:Processing batch 54/796
INFO:root:Processing batch 55/796
INFO:root:Processing batch 56/796
INFO:root:Processing batch 57/796
INFO:root:Processing batch 58/796
INFO:root:Processing batch 59/796
INFO:root:Processing batch 60/796
INFO:root:Processing batch 61/796
INFO:root:Processing batch 62/796
INFO:root:Processing batch 63/796
INFO:root:Processing batch 64/796
INFO:root:Processing batch 65/796
INFO:root:Processing batch 66/796
INFO:root:Processing batch 67/796
INFO:root:Processing batch 68/796
INFO:root:Processing batch 69/796
INFO:root:Processing batch 70/796
INFO:root:Processing batch 71/796
INFO:root:Processing batch 72/796
INFO:root:Processing batch 73/796
INFO:root:Processing batch 74/796
INFO:root:Processing batch 75/796
INFO:root:Processing batch 76/796
INFO:root:Processing batch 77/796
INFO:root:Processing batch 78/796
INFO:root:Processing batch 79/796
INFO:root:Processing batch 80/796
INFO:root:Processing batch 81/796
INFO:root:Processing batch 82/796
INFO:root:Processing batch 83/796
INFO:root:Processing batch 84/796
INFO:root:Processing batch 85/796
INFO:root:Processing batch 86/796
INFO:root:Processing batch 87/796
INFO:root:Processing batch 88/796
INFO:root:Processing batch 89/796
INFO:root:Processing batch 90/796
INFO:root:Processing batch 91/796
INFO:root:Processing batch 92/796
INFO:root:Processing batch 93/796
INFO:root:Processing batch 94/796
INFO:root:Processing batch 95/796
INFO:root:Processing batch 96/796
INFO:root:Processing batch 97/796
INFO:root:Processing batch 98/796
INFO:root:Processing batch 99/796
INFO:root:Processing batch 100/796
INFO:root:Processing batch 101/796
INFO:root:Processing batch 102/796
INFO:root:Processing batch 103/796
INFO:root:Processing batch 104/796
INFO:root:Processing batch 105/796
INFO:root:Processing batch 106/796
INFO:root:Processing batch 107/796
INFO:root:Processing batch 108/796
INFO:root:Processing batch 109/796
INFO:root:Processing batch 110/796
INFO:root:Processing batch 111/796
INFO:root:Processing batch 112/796
INFO:root:Processing batch 113/796
INFO:root:Processing batch 114/796
INFO:root:Processing batch 115/796
INFO:root:Processing batch 116/796
INFO:root:Processing batch 117/796
INFO:root:Processing batch 118/796
INFO:root:Processing batch 119/796
INFO:root:Processing batch 120/796
INFO:root:Processing batch 121/796
INFO:root:Processing batch 122/796
INFO:root:Processing batch 123/796
INFO:root:Processing batch 124/796
INFO:root:Processing batch 125/796
INFO:root:Processing batch 126/796
INFO:root:Processing batch 127/796
INFO:root:Processing batch 128/796
INFO:root:Processing batch 129/796
INFO:root:Processing batch 130/796
INFO:root:Processing batch 131/796
INFO:root:Processing batch 132/796
INFO:root:Processing batch 133/796
INFO:root:Processing batch 134/796
INFO:root:Processing batch 135/796
INFO:root:Processing batch 136/796
INFO:root:Processing batch 137/796
INFO:root:Processing batch 138/796
INFO:root:Processing batch 139/796
INFO:root:Processing batch 140/796
INFO:root:Processing batch 141/796
INFO:root:Processing batch 142/796
INFO:root:Processing batch 143/796
INFO:root:Processing batch 144/796
INFO:root:Processing batch 145/796
INFO:root:Processing batch 146/796
INFO:root:Processing batch 147/796
INFO:root:Processing batch 148/796
INFO:root:Processing batch 149/796
INFO:root:Processing batch 150/796
INFO:root:Processing batch 151/796
INFO:root:Processing batch 152/796
INFO:root:Processing batch 153/796
INFO:root:Processing batch 154/796
INFO:root:Processing batch 155/796
INFO:root:Processing batch 156/796
INFO:root:Processing batch 157/796
INFO:root:Processing batch 158/796
INFO:root:Processing batch 159/796
INFO:root:Processing batch 160/796
INFO:root:Processing batch 161/796
INFO:root:Processing batch 162/796
INFO:root:Processing batch 163/796
INFO:root:Processing batch 164/796
INFO:root:Processing batch 165/796
INFO:root:Processing batch 166/796
INFO:root:Processing batch 167/796
INFO:root:Processing batch 168/796
INFO:root:Processing batch 169/796
INFO:root:Processing batch 170/796
INFO:root:Processing batch 171/796
INFO:root:Processing batch 172/796
INFO:root:Processing batch 173/796
INFO:root:Processing batch 174/796
INFO:root:Processing batch 175/796
INFO:root:Processing batch 176/796
INFO:root:Processing batch 177/796
INFO:root:Processing batch 178/796
INFO:root:Processing batch 179/796
INFO:root:Processing batch 180/796
INFO:root:Processing batch 181/796
INFO:root:Processing batch 182/796
INFO:root:Processing batch 183/796
INFO:root:Processing batch 184/796
INFO:root:Processing batch 185/796
INFO:root:Processing batch 186/796
INFO:root:Processing batch 187/796
INFO:root:Processing batch 188/796
INFO:root:Processing batch 189/796
INFO:root:Processing batch 190/796
INFO:root:Processing batch 191/796
INFO:root:Processing batch 192/796
INFO:root:Processing batch 193/796
INFO:root:Processing batch 194/796
INFO:root:Processing batch 195/796
INFO:root:Processing batch 196/796
INFO:root:Processing batch 197/796
INFO:root:Processing batch 198/796
INFO:root:Processing batch 199/796
INFO:root:Processing batch 200/796
INFO:root:Processing batch 201/796
INFO:root:Processing batch 202/796
INFO:root:Processing batch 203/796
INFO:root:Processing batch 204/796
INFO:root:Processing batch 205/796
INFO:root:Processing batch 206/796
INFO:root:Processing batch 207/796
INFO:root:Processing batch 208/796
INFO:root:Processing batch 209/796
INFO:root:Processing batch 210/796
INFO:root:Processing batch 211/796
INFO:root:Processing batch 212/796
INFO:root:Processing batch 213/796
INFO:root:Processing batch 214/796
INFO:root:Processing batch 215/796
INFO:root:Processing batch 216/796
INFO:root:Processing batch 217/796
INFO:root:Processing batch 218/796
INFO:root:Processing batch 219/796
INFO:root:Processing batch 220/796
INFO:root:Processing batch 221/796
INFO:root:Processing batch 222/796
INFO:root:Processing batch 223/796
INFO:root:Processing batch 224/796
INFO:root:Processing batch 225/796
INFO:root:Processing batch 226/796
INFO:root:Processing batch 227/796
INFO:root:Processing batch 228/796
INFO:root:Processing batch 229/796
INFO:root:Processing batch 230/796
INFO:root:Processing batch 231/796
INFO:root:Processing batch 232/796
INFO:root:Processing batch 233/796
INFO:root:Processing batch 234/796
INFO:root:Processing batch 235/796
INFO:root:Processing batch 236/796
INFO:root:Processing batch 237/796
INFO:root:Processing batch 238/796
INFO:root:Processing batch 239/796
INFO:root:Processing batch 240/796
INFO:root:Processing batch 241/796
INFO:root:Processing batch 242/796
INFO:root:Processing batch 243/796
INFO:root:Processing batch 244/796
INFO:root:Processing batch 245/796
INFO:root:Processing batch 246/796
INFO:root:Processing batch 247/796
INFO:root:Processing batch 248/796
INFO:root:Processing batch 249/796
INFO:root:Processing batch 250/796
INFO:root:Processing batch 251/796
INFO:root:Processing batch 252/796
INFO:root:Processing batch 253/796
INFO:root:Processing batch 254/796
INFO:root:Processing batch 255/796
INFO:root:Processing batch 256/796
INFO:root:Processing batch 257/796
INFO:root:Processing batch 258/796
INFO:root:Processing batch 259/796
INFO:root:Processing batch 260/796
INFO:root:Processing batch 261/796
INFO:root:Processing batch 262/796
INFO:root:Processing batch 263/796
INFO:root:Processing batch 264/796
INFO:root:Processing batch 265/796
INFO:root:Processing batch 266/796
INFO:root:Processing batch 267/796
INFO:root:Processing batch 268/796
INFO:root:Processing batch 269/796
INFO:root:Processing batch 270/796
INFO:root:Processing batch 271/796
INFO:root:Processing batch 272/796
INFO:root:Processing batch 273/796
INFO:root:Processing batch 274/796
INFO:root:Processing batch 275/796
INFO:root:Processing batch 276/796
INFO:root:Processing batch 277/796
INFO:root:Processing batch 278/796
INFO:root:Processing batch 279/796
INFO:root:Processing batch 280/796
INFO:root:Processing batch 281/796
INFO:root:Processing batch 282/796
INFO:root:Processing batch 283/796
INFO:root:Processing batch 284/796
INFO:root:Processing batch 285/796
INFO:root:Processing batch 286/796
INFO:root:Processing batch 287/796
INFO:root:Processing batch 288/796
INFO:root:Processing batch 289/796
INFO:root:Processing batch 290/796
INFO:root:Processing batch 291/796
INFO:root:Processing batch 292/796
INFO:root:Processing batch 293/796
INFO:root:Processing batch 294/796
INFO:root:Processing batch 295/796
INFO:root:Processing batch 296/796
INFO:root:Processing batch 297/796
INFO:root:Processing batch 298/796
INFO:root:Processing batch 299/796
INFO:root:Processing batch 300/796
INFO:root:Processing batch 301/796
INFO:root:Processing batch 302/796
INFO:root:Processing batch 303/796
INFO:root:Processing batch 304/796
INFO:root:Processing batch 305/796
INFO:root:Processing batch 306/796
INFO:root:Processing batch 307/796
INFO:root:Processing batch 308/796
INFO:root:Processing batch 309/796
INFO:root:Processing batch 310/796
INFO:root:Processing batch 311/796
INFO:root:Processing batch 312/796
INFO:root:Processing batch 313/796
INFO:root:Processing batch 314/796
INFO:root:Processing batch 315/796
INFO:root:Processing batch 316/796
INFO:root:Processing batch 317/796
INFO:root:Processing batch 318/796
INFO:root:Processing batch 319/796
INFO:root:Processing batch 320/796
INFO:root:Processing batch 321/796
INFO:root:Processing batch 322/796
INFO:root:Processing batch 323/796
INFO:root:Processing batch 324/796
INFO:root:Processing batch 325/796
INFO:root:Processing batch 326/796
INFO:root:Processing batch 327/796
INFO:root:Processing batch 328/796
INFO:root:Processing batch 329/796
INFO:root:Processing batch 330/796
INFO:root:Processing batch 331/796
INFO:root:Processing batch 332/796
INFO:root:Processing batch 333/796
INFO:root:Processing batch 334/796
INFO:root:Processing batch 335/796
INFO:root:Processing batch 336/796
INFO:root:Processing batch 337/796
INFO:root:Processing batch 338/796
INFO:root:Processing batch 339/796
INFO:root:Processing batch 340/796
INFO:root:Processing batch 341/796
INFO:root:Processing batch 342/796
INFO:root:Processing batch 343/796
INFO:root:Processing batch 344/796
INFO:root:Processing batch 345/796
INFO:root:Processing batch 346/796
INFO:root:Processing batch 347/796
INFO:root:Processing batch 348/796
INFO:root:Processing batch 349/796
INFO:root:Processing batch 350/796
INFO:root:Processing batch 351/796
INFO:root:Processing batch 352/796
INFO:root:Processing batch 353/796
INFO:root:Processing batch 354/796
INFO:root:Processing batch 355/796
INFO:root:Processing batch 356/796
INFO:root:Processing batch 357/796
INFO:root:Processing batch 358/796
INFO:root:Processing batch 359/796
INFO:root:Processing batch 360/796
INFO:root:Processing batch 361/796
INFO:root:Processing batch 362/796
INFO:root:Processing batch 363/796
INFO:root:Processing batch 364/796
INFO:root:Processing batch 365/796
INFO:root:Processing batch 366/796
INFO:root:Processing batch 367/796
INFO:root:Processing batch 368/796
INFO:root:Processing batch 369/796
INFO:root:Processing batch 370/796
INFO:root:Processing batch 371/796
INFO:root:Processing batch 372/796
INFO:root:Processing batch 373/796
INFO:root:Processing batch 374/796
INFO:root:Processing batch 375/796
INFO:root:Processing batch 376/796
INFO:root:Processing batch 377/796
INFO:root:Processing batch 378/796
INFO:root:Processing batch 379/796
INFO:root:Processing batch 380/796
INFO:root:Processing batch 381/796
INFO:root:Processing batch 382/796
INFO:root:Processing batch 383/796
INFO:root:Processing batch 384/796
INFO:root:Processing batch 385/796
INFO:root:Processing batch 386/796
INFO:root:Processing batch 387/796
INFO:root:Processing batch 388/796
INFO:root:Processing batch 389/796
INFO:root:Processing batch 390/796
INFO:root:Processing batch 391/796
INFO:root:Processing batch 392/796
INFO:root:Processing batch 393/796
INFO:root:Processing batch 394/796
INFO:root:Processing batch 395/796
INFO:root:Processing batch 396/796
INFO:root:Processing batch 397/796
INFO:root:Processing batch 398/796
INFO:root:Processing batch 399/796
INFO:root:Processing batch 400/796
INFO:root:Processing batch 401/796
INFO:root:Processing batch 402/796
INFO:root:Processing batch 403/796
INFO:root:Processing batch 404/796
INFO:root:Processing batch 405/796
INFO:root:Processing batch 406/796
INFO:root:Processing batch 407/796
INFO:root:Processing batch 408/796
INFO:root:Processing batch 409/796
INFO:root:Processing batch 410/796
INFO:root:Processing batch 411/796
INFO:root:Processing batch 412/796
INFO:root:Processing batch 413/796
INFO:root:Processing batch 414/796
INFO:root:Processing batch 415/796
INFO:root:Processing batch 416/796
INFO:root:Processing batch 417/796
INFO:root:Processing batch 418/796
INFO:root:Processing batch 419/796
INFO:root:Processing batch 420/796
INFO:root:Processing batch 421/796
INFO:root:Processing batch 422/796
INFO:root:Processing batch 423/796
INFO:root:Processing batch 424/796
INFO:root:Processing batch 425/796
INFO:root:Processing batch 426/796
INFO:root:Processing batch 427/796
INFO:root:Processing batch 428/796
INFO:root:Processing batch 429/796
INFO:root:Processing batch 430/796
INFO:root:Processing batch 431/796
INFO:root:Processing batch 432/796
INFO:root:Processing batch 433/796
INFO:root:Processing batch 434/796
INFO:root:Processing batch 435/796
INFO:root:Processing batch 436/796
INFO:root:Processing batch 437/796
INFO:root:Processing batch 438/796
INFO:root:Processing batch 439/796
INFO:root:Processing batch 440/796
INFO:root:Processing batch 441/796
INFO:root:Processing batch 442/796
INFO:root:Processing batch 443/796
INFO:root:Processing batch 444/796
INFO:root:Processing batch 445/796
INFO:root:Processing batch 446/796
INFO:root:Processing batch 447/796
INFO:root:Processing batch 448/796
INFO:root:Processing batch 449/796
INFO:root:Processing batch 450/796
INFO:root:Processing batch 451/796
INFO:root:Processing batch 452/796
INFO:root:Processing batch 453/796
INFO:root:Processing batch 454/796
INFO:root:Processing batch 455/796
INFO:root:Processing batch 456/796
INFO:root:Processing batch 457/796
INFO:root:Processing batch 458/796
INFO:root:Processing batch 459/796
INFO:root:Processing batch 460/796
INFO:root:Processing batch 461/796
INFO:root:Processing batch 462/796
INFO:root:Processing batch 463/796
INFO:root:Processing batch 464/796
INFO:root:Processing batch 465/796
INFO:root:Processing batch 466/796
INFO:root:Processing batch 467/796
INFO:root:Processing batch 468/796
INFO:root:Processing batch 469/796
INFO:root:Processing batch 470/796
INFO:root:Processing batch 471/796
INFO:root:Processing batch 472/796
INFO:root:Processing batch 473/796
INFO:root:Processing batch 474/796
INFO:root:Processing batch 475/796
INFO:root:Processing batch 476/796
INFO:root:Processing batch 477/796
INFO:root:Processing batch 478/796
INFO:root:Processing batch 479/796
INFO:root:Processing batch 480/796
INFO:root:Processing batch 481/796
INFO:root:Processing batch 482/796
INFO:root:Processing batch 483/796
INFO:root:Processing batch 484/796
INFO:root:Processing batch 485/796
INFO:root:Processing batch 486/796
INFO:root:Processing batch 487/796
INFO:root:Processing batch 488/796
INFO:root:Processing batch 489/796
INFO:root:Processing batch 490/796
INFO:root:Processing batch 491/796
INFO:root:Processing batch 492/796
INFO:root:Processing batch 493/796
INFO:root:Processing batch 494/796
INFO:root:Processing batch 495/796
INFO:root:Processing batch 496/796
INFO:root:Processing batch 497/796
INFO:root:Processing batch 498/796
INFO:root:Processing batch 499/796
INFO:root:Processing batch 500/796
INFO:root:Processing batch 501/796
INFO:root:Processing batch 502/796
INFO:root:Processing batch 503/796
INFO:root:Processing batch 504/796
INFO:root:Processing batch 505/796
INFO:root:Processing batch 506/796
INFO:root:Processing batch 507/796
INFO:root:Processing batch 508/796
INFO:root:Processing batch 509/796
INFO:root:Processing batch 510/796
INFO:root:Processing batch 511/796
INFO:root:Processing batch 512/796
INFO:root:Processing batch 513/796
INFO:root:Processing batch 514/796
INFO:root:Processing batch 515/796
INFO:root:Processing batch 516/796
INFO:root:Processing batch 517/796
INFO:root:Processing batch 518/796
INFO:root:Processing batch 519/796
INFO:root:Processing batch 520/796
INFO:root:Processing batch 521/796
INFO:root:Processing batch 522/796
INFO:root:Processing batch 523/796
INFO:root:Processing batch 524/796
INFO:root:Processing batch 525/796
INFO:root:Processing batch 526/796
INFO:root:Processing batch 527/796
INFO:root:Processing batch 528/796
INFO:root:Processing batch 529/796
INFO:root:Processing batch 530/796
INFO:root:Processing batch 531/796
INFO:root:Processing batch 532/796
INFO:root:Processing batch 533/796
INFO:root:Processing batch 534/796
INFO:root:Processing batch 535/796
INFO:root:Processing batch 536/796
INFO:root:Processing batch 537/796
INFO:root:Processing batch 538/796
INFO:root:Processing batch 539/796
INFO:root:Processing batch 540/796
INFO:root:Processing batch 541/796
INFO:root:Processing batch 542/796
INFO:root:Processing batch 543/796
INFO:root:Processing batch 544/796
INFO:root:Processing batch 545/796
INFO:root:Processing batch 546/796
INFO:root:Processing batch 547/796
INFO:root:Processing batch 548/796
INFO:root:Processing batch 549/796
INFO:root:Processing batch 550/796
INFO:root:Processing batch 551/796
INFO:root:Processing batch 552/796
INFO:root:Processing batch 553/796
INFO:root:Processing batch 554/796
INFO:root:Processing batch 555/796
INFO:root:Processing batch 556/796
INFO:root:Processing batch 557/796
INFO:root:Processing batch 558/796
INFO:root:Processing batch 559/796
INFO:root:Processing batch 560/796
INFO:root:Processing batch 561/796
INFO:root:Processing batch 562/796
INFO:root:Processing batch 563/796
INFO:root:Processing batch 564/796
INFO:root:Processing batch 565/796
INFO:root:Processing batch 566/796
INFO:root:Processing batch 567/796
INFO:root:Processing batch 568/796
INFO:root:Processing batch 569/796
INFO:root:Processing batch 570/796
INFO:root:Processing batch 571/796
INFO:root:Processing batch 572/796
INFO:root:Processing batch 573/796
INFO:root:Processing batch 574/796
INFO:root:Processing batch 575/796
INFO:root:Processing batch 576/796
INFO:root:Processing batch 577/796
INFO:root:Processing batch 578/796
INFO:root:Processing batch 579/796
INFO:root:Processing batch 580/796
INFO:root:Processing batch 581/796
INFO:root:Processing batch 582/796
INFO:root:Processing batch 583/796
INFO:root:Processing batch 584/796
INFO:root:Processing batch 585/796
INFO:root:Processing batch 586/796
INFO:root:Processing batch 587/796
INFO:root:Processing batch 588/796
INFO:root:Processing batch 589/796
INFO:root:Processing batch 590/796
INFO:root:Processing batch 591/796
INFO:root:Processing batch 592/796
INFO:root:Processing batch 593/796
INFO:root:Processing batch 594/796
INFO:root:Processing batch 595/796
INFO:root:Processing batch 596/796
INFO:root:Processing batch 597/796
INFO:root:Processing batch 598/796
INFO:root:Processing batch 599/796
INFO:root:Processing batch 600/796
INFO:root:Processing batch 601/796
INFO:root:Processing batch 602/796
INFO:root:Processing batch 603/796
INFO:root:Processing batch 604/796
INFO:root:Processing batch 605/796
INFO:root:Processing batch 606/796
INFO:root:Processing batch 607/796
INFO:root:Processing batch 608/796
INFO:root:Processing batch 609/796
INFO:root:Processing batch 610/796
INFO:root:Processing batch 611/796
INFO:root:Processing batch 612/796
INFO:root:Processing batch 613/796
INFO:root:Processing batch 614/796
INFO:root:Processing batch 615/796
INFO:root:Processing batch 616/796
INFO:root:Processing batch 617/796
INFO:root:Processing batch 618/796
INFO:root:Processing batch 619/796
INFO:root:Processing batch 620/796
INFO:root:Processing batch 621/796
INFO:root:Processing batch 622/796
INFO:root:Processing batch 623/796
INFO:root:Processing batch 624/796
INFO:root:Processing batch 625/796
INFO:root:Processing batch 626/796
INFO:root:Processing batch 627/796
INFO:root:Processing batch 628/796
INFO:root:Processing batch 629/796
INFO:root:Processing batch 630/796
INFO:root:Processing batch 631/796
INFO:root:Processing batch 632/796
INFO:root:Processing batch 633/796
INFO:root:Processing batch 634/796
INFO:root:Processing batch 635/796
INFO:root:Processing batch 636/796
INFO:root:Processing batch 637/796
INFO:root:Processing batch 638/796
INFO:root:Processing batch 639/796
INFO:root:Processing batch 640/796
INFO:root:Processing batch 641/796
INFO:root:Processing batch 642/796
INFO:root:Processing batch 643/796
INFO:root:Processing batch 644/796
INFO:root:Processing batch 645/796
INFO:root:Processing batch 646/796
INFO:root:Processing batch 647/796
INFO:root:Processing batch 648/796
INFO:root:Processing batch 649/796
INFO:root:Processing batch 650/796
INFO:root:Processing batch 651/796
INFO:root:Processing batch 652/796
INFO:root:Processing batch 653/796
INFO:root:Processing batch 654/796
INFO:root:Processing batch 655/796
INFO:root:Processing batch 656/796
INFO:root:Processing batch 657/796
INFO:root:Processing batch 658/796
INFO:root:Processing batch 659/796
INFO:root:Processing batch 660/796
INFO:root:Processing batch 661/796
INFO:root:Processing batch 662/796
INFO:root:Processing batch 663/796
INFO:root:Processing batch 664/796
INFO:root:Processing batch 665/796
INFO:root:Processing batch 666/796
INFO:root:Processing batch 667/796
INFO:root:Processing batch 668/796
INFO:root:Processing batch 669/796
INFO:root:Processing batch 670/796
INFO:root:Processing batch 671/796
INFO:root:Processing batch 672/796
INFO:root:Processing batch 673/796
INFO:root:Processing batch 674/796
INFO:root:Processing batch 675/796
INFO:root:Processing batch 676/796
INFO:root:Processing batch 677/796
INFO:root:Processing batch 678/796
INFO:root:Processing batch 679/796
INFO:root:Processing batch 680/796
INFO:root:Processing batch 681/796
INFO:root:Processing batch 682/796
INFO:root:Processing batch 683/796
INFO:root:Processing batch 684/796
INFO:root:Processing batch 685/796
INFO:root:Processing batch 686/796
INFO:root:Processing batch 687/796
INFO:root:Processing batch 688/796
INFO:root:Processing batch 689/796
INFO:root:Processing batch 690/796
INFO:root:Processing batch 691/796
INFO:root:Processing batch 692/796
INFO:root:Processing batch 693/796
INFO:root:Processing batch 694/796
INFO:root:Processing batch 695/796
INFO:root:Processing batch 696/796
INFO:root:Processing batch 697/796
INFO:root:Processing batch 698/796
INFO:root:Processing batch 699/796
INFO:root:Processing batch 700/796
INFO:root:Processing batch 701/796
INFO:root:Processing batch 702/796
INFO:root:Processing batch 703/796
INFO:root:Processing batch 704/796
INFO:root:Processing batch 705/796
INFO:root:Processing batch 706/796
INFO:root:Processing batch 707/796
INFO:root:Processing batch 708/796
INFO:root:Processing batch 709/796
INFO:root:Processing batch 710/796
INFO:root:Processing batch 711/796
INFO:root:Processing batch 712/796
INFO:root:Processing batch 713/796
INFO:root:Processing batch 714/796
INFO:root:Processing batch 715/796
INFO:root:Processing batch 716/796
INFO:root:Processing batch 717/796
INFO:root:Processing batch 718/796
INFO:root:Processing batch 719/796
INFO:root:Processing batch 720/796
INFO:root:Processing batch 721/796
INFO:root:Processing batch 722/796
INFO:root:Processing batch 723/796
INFO:root:Processing batch 724/796
INFO:root:Processing batch 725/796
INFO:root:Processing batch 726/796
INFO:root:Processing batch 727/796
INFO:root:Processing batch 728/796
INFO:root:Processing batch 729/796
INFO:root:Processing batch 730/796
INFO:root:Processing batch 731/796
INFO:root:Processing batch 732/796
INFO:root:Processing batch 733/796
INFO:root:Processing batch 734/796
INFO:root:Processing batch 735/796
INFO:root:Processing batch 736/796
INFO:root:Processing batch 737/796
INFO:root:Processing batch 738/796
INFO:root:Processing batch 739/796
INFO:root:Processing batch 740/796
INFO:root:Processing batch 741/796
INFO:root:Processing batch 742/796
INFO:root:Processing batch 743/796
INFO:root:Processing batch 744/796
INFO:root:Processing batch 745/796
INFO:root:Processing batch 746/796
INFO:root:Processing batch 747/796
INFO:root:Processing batch 748/796
INFO:root:Processing batch 749/796
INFO:root:Processing batch 750/796
INFO:root:Processing batch 751/796
INFO:root:Processing batch 752/796
INFO:root:Processing batch 753/796
INFO:root:Processing batch 754/796
INFO:root:Processing batch 755/796
INFO:root:Processing batch 756/796
INFO:root:Processing batch 757/796
INFO:root:Processing batch 758/796
INFO:root:Processing batch 759/796
INFO:root:Processing batch 760/796
INFO:root:Processing batch 761/796
INFO:root:Processing batch 762/796
INFO:root:Processing batch 763/796
INFO:root:Processing batch 764/796
INFO:root:Processing batch 765/796
INFO:root:Processing batch 766/796
INFO:root:Processing batch 767/796
INFO:root:Processing batch 768/796
INFO:root:Processing batch 769/796
INFO:root:Processing batch 770/796
INFO:root:Processing batch 771/796
INFO:root:Processing batch 772/796
INFO:root:Processing batch 773/796
INFO:root:Processing batch 774/796
INFO:root:Processing batch 775/796
INFO:root:Processing batch 776/796
INFO:root:Processing batch 777/796
INFO:root:Processing batch 778/796
INFO:root:Processing batch 779/796
INFO:root:Processing batch 780/796
INFO:root:Processing batch 781/796
INFO:root:Processing batch 782/796
INFO:root:Processing batch 783/796
INFO:root:Processing batch 784/796
INFO:root:Processing batch 785/796
INFO:root:Processing batch 786/796
INFO:root:Processing batch 787/796
INFO:root:Processing batch 788/796
INFO:root:Processing batch 789/796
INFO:root:Processing batch 790/796
INFO:root:Processing batch 791/796
INFO:root:Processing batch 792/796
INFO:root:Processing batch 793/796
INFO:root:Processing batch 794/796
INFO:root:Processing batch 795/796
INFO:root:Processing batch 796/796
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4748101532459259, 0.41967248916625977, 0.35907915234565735], 'std': [0.279197633266449, 0.27405133843421936, 0.2634223997592926], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4748101532459259, 0.41967248916625977, 0.35907915234565735], std=[0.279197633266449, 0.27405133843421936, 0.2634223997592926])']}}}
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 179MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.13957
INFO:root:Training epoch 1, Iteration 30, Loss: 4.98663
INFO:root:Training epoch 1, Iteration 60, Loss: 5.00514
INFO:root:Training epoch 1, Iteration 90, Loss: 4.92000
INFO:root:Training epoch 1, Iteration 120, Loss: 4.73206
INFO:root:Training epoch 1, Iteration 150, Loss: 4.74670
INFO:root:Training epoch 1, Iteration 180, Loss: 4.66201
INFO:root:Training epoch 1, Iteration 210, Loss: 4.57101
INFO:root:Training epoch 1, Iteration 240, Loss: 4.55975
INFO:root:Training epoch 1, Iteration 270, Loss: 4.47589
INFO:root:Training epoch 1, Iteration 300, Loss: 4.41926
INFO:root:Training epoch 1, Iteration 330, Loss: 4.46469
INFO:root:Training epoch 1, Iteration 360, Loss: 4.42474
INFO:root:Training epoch 1, Iteration 390, Loss: 4.43746
INFO:root:Training epoch 1, Iteration 420, Loss: 4.46538
INFO:root:Training epoch 1, Iteration 450, Loss: 4.26193
INFO:root:Training epoch 1, Iteration 480, Loss: 4.24449
INFO:root:Training epoch 1, Iteration 510, Loss: 4.42051
INFO:root:Training epoch 1, Iteration 540, Loss: 4.19552
INFO:root:Training epoch 1, Iteration 570, Loss: 4.17137
INFO:root:Training epoch 1, Iteration 600, Loss: 4.37614
INFO:root:Training epoch 1, Iteration 630, Loss: 4.21376
INFO:root:Training epoch 1, Iteration 660, Loss: 4.27773
INFO:root:Training epoch 1, Iteration 690, Loss: 4.31369
INFO:root:Training epoch 1, Iteration 720, Loss: 4.21526
INFO:root:Training epoch 1, Iteration 750, Loss: 4.22454
INFO:root:Training epoch 1, Iteration 780, Loss: 4.12245
INFO:root:Validation iteration 1, Loss: 4.52269
INFO:root:Validation iteration 10, Loss: 4.24125
INFO:root:Validation iteration 20, Loss: 4.05020
INFO:root:Validation iteration 30, Loss: 4.22466
INFO:root:Validation iteration 40, Loss: 3.93454
INFO:root:Validation iteration 50, Loss: 4.06918
INFO:root:Validation iteration 60, Loss: 4.29266
INFO:root:Validation iteration 70, Loss: 4.00395
INFO:root:Validation iteration 80, Loss: 4.04861
INFO:root:Validation iteration 90, Loss: 3.91531
INFO:root:Validation iteration 100, Loss: 4.27245
INFO:root:Validation iteration 110, Loss: 4.37999
INFO:root:Validation iteration 120, Loss: 3.95135
INFO:root:Validation iteration 130, Loss: 4.21212
INFO:root:Validation iteration 140, Loss: 4.14856
INFO:root:Validation iteration 150, Loss: 4.21601
INFO:root:Validation iteration 160, Loss: 4.08768
INFO:root:Validation iteration 170, Loss: 4.23917
INFO:root:Validation iteration 180, Loss: 4.33498
INFO:root:Validation iteration 190, Loss: 3.94209
INFO:root:Validation iteration 200, Loss: 3.98016
INFO:root:Validation iteration 210, Loss: 3.91621
INFO:root:Validation iteration 220, Loss: 4.05289
INFO:root:Validation iteration 230, Loss: 4.36075
INFO:root:Validation iteration 240, Loss: 4.28784
INFO:root:Validation iteration 250, Loss: 4.15603
INFO:root:Validation iteration 260, Loss: 4.35400
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.452
INFO:root:Validation accuracy: 0.066, Validation loss: 4.13825
INFO:root:Training epoch 2, Iteration 1, Loss: 3.96606
INFO:root:Training epoch 2, Iteration 30, Loss: 4.01647
INFO:root:Training epoch 2, Iteration 60, Loss: 4.07309
INFO:root:Training epoch 2, Iteration 90, Loss: 4.11294
INFO:root:Training epoch 2, Iteration 120, Loss: 4.09336
INFO:root:Training epoch 2, Iteration 150, Loss: 4.23011
INFO:root:Training epoch 2, Iteration 180, Loss: 4.17297
INFO:root:Training epoch 2, Iteration 210, Loss: 4.03277
INFO:root:Training epoch 2, Iteration 240, Loss: 4.20495
INFO:root:Training epoch 2, Iteration 270, Loss: 4.02988
INFO:root:Training epoch 2, Iteration 300, Loss: 4.08120
INFO:root:Training epoch 2, Iteration 330, Loss: 4.06022
INFO:root:Training epoch 2, Iteration 360, Loss: 4.05220
INFO:root:Training epoch 2, Iteration 390, Loss: 3.90068
INFO:root:Training epoch 2, Iteration 420, Loss: 4.02327
INFO:root:Training epoch 2, Iteration 450, Loss: 3.95897
INFO:root:Training epoch 2, Iteration 480, Loss: 4.11177
INFO:root:Training epoch 2, Iteration 510, Loss: 3.96660
INFO:root:Training epoch 2, Iteration 540, Loss: 4.03327
INFO:root:Training epoch 2, Iteration 570, Loss: 3.94340
INFO:root:Training epoch 2, Iteration 600, Loss: 3.93460
INFO:root:Training epoch 2, Iteration 630, Loss: 3.86549
INFO:root:Training epoch 2, Iteration 660, Loss: 3.92486
INFO:root:Training epoch 2, Iteration 690, Loss: 4.01911
INFO:root:Training epoch 2, Iteration 720, Loss: 3.91674
INFO:root:Training epoch 2, Iteration 750, Loss: 3.86331
INFO:root:Training epoch 2, Iteration 780, Loss: 4.11580
INFO:root:Validation iteration 1, Loss: 4.52148
INFO:root:Validation iteration 10, Loss: 4.06051
INFO:root:Validation iteration 20, Loss: 3.87113
INFO:root:Validation iteration 30, Loss: 3.95398
INFO:root:Validation iteration 40, Loss: 3.93674
INFO:root:Validation iteration 50, Loss: 4.00521
INFO:root:Validation iteration 60, Loss: 3.72009
INFO:root:Validation iteration 70, Loss: 3.83184
INFO:root:Validation iteration 80, Loss: 3.88859
INFO:root:Validation iteration 90, Loss: 3.62266
INFO:root:Validation iteration 100, Loss: 4.03266
INFO:root:Validation iteration 110, Loss: 4.08180
INFO:root:Validation iteration 120, Loss: 3.80439
INFO:root:Validation iteration 130, Loss: 3.96661
INFO:root:Validation iteration 140, Loss: 3.90630
INFO:root:Validation iteration 150, Loss: 3.97038
INFO:root:Validation iteration 160, Loss: 3.94952
INFO:root:Validation iteration 170, Loss: 3.88096
INFO:root:Validation iteration 180, Loss: 4.05134
INFO:root:Validation iteration 190, Loss: 3.73626
INFO:root:Validation iteration 200, Loss: 3.89747
INFO:root:Validation iteration 210, Loss: 3.76141
INFO:root:Validation iteration 220, Loss: 3.91282
INFO:root:Validation iteration 230, Loss: 4.07477
INFO:root:Validation iteration 240, Loss: 3.96699
INFO:root:Validation iteration 250, Loss: 4.01604
INFO:root:Validation iteration 260, Loss: 3.95624
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.030
INFO:root:Validation accuracy: 0.099, Validation loss: 3.91224
INFO:root:Best validation accuracy: 0.099 at epoch 2
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.74171
INFO:root:Validation iteration 10, Loss: 3.96772
INFO:root:Validation iteration 20, Loss: 4.12167
INFO:root:Validation iteration 30, Loss: 4.25198
INFO:root:Validation iteration 40, Loss: 3.91488
INFO:root:Validation iteration 50, Loss: 3.93195
INFO:root:Validation iteration 60, Loss: 3.81178
INFO:root:Validation iteration 70, Loss: 3.90187
INFO:root:Validation iteration 80, Loss: 4.20231
INFO:root:Validation iteration 90, Loss: 3.67766
INFO:root:Validation iteration 100, Loss: 3.85151
INFO:root:Validation iteration 110, Loss: 3.93422
INFO:root:Validation iteration 120, Loss: 3.73357
INFO:root:Validation iteration 130, Loss: 3.77690
INFO:root:Validation iteration 140, Loss: 3.96078
INFO:root:Validation iteration 150, Loss: 3.77702
INFO:root:Validation iteration 160, Loss: 3.76361
INFO:root:Validation iteration 170, Loss: 3.80420
INFO:root:Validation iteration 180, Loss: 4.09083
INFO:root:Validation iteration 190, Loss: 3.65259
INFO:root:Validation iteration 200, Loss: 3.91601
INFO:root:Validation iteration 210, Loss: 3.85064
INFO:root:Validation iteration 220, Loss: 4.06520
INFO:root:Validation iteration 230, Loss: 3.84432
INFO:root:Validation iteration 240, Loss: 4.01834
INFO:root:Validation iteration 250, Loss: 4.01139
INFO:root:Validation iteration 260, Loss: 3.87737
Test accuracy: 0.123, Test loss: 3.91555
INFO:root:Saving results...
INFO:root:Done!
"""

string18 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', test_root='./data/kaggle_test', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.', trained_model_path='./temp/best_model_3.pth', predictions_path='./temp/predictions.csv'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size=32, train_split_size=0.75), 'train': TrainConfig(num_epochs=6, train_log_frequency=20, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False, save=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/398
INFO:root:Processing batch 2/398
INFO:root:Processing batch 3/398
INFO:root:Processing batch 4/398
INFO:root:Processing batch 5/398
INFO:root:Processing batch 6/398
INFO:root:Processing batch 7/398
INFO:root:Processing batch 8/398
INFO:root:Processing batch 9/398
INFO:root:Processing batch 10/398
INFO:root:Processing batch 11/398
INFO:root:Processing batch 12/398
INFO:root:Processing batch 13/398
INFO:root:Processing batch 14/398
INFO:root:Processing batch 15/398
INFO:root:Processing batch 16/398
INFO:root:Processing batch 17/398
INFO:root:Processing batch 18/398
INFO:root:Processing batch 19/398
INFO:root:Processing batch 20/398
INFO:root:Processing batch 21/398
INFO:root:Processing batch 22/398
INFO:root:Processing batch 23/398
INFO:root:Processing batch 24/398
INFO:root:Processing batch 25/398
INFO:root:Processing batch 26/398
INFO:root:Processing batch 27/398
INFO:root:Processing batch 28/398
INFO:root:Processing batch 29/398
INFO:root:Processing batch 30/398
INFO:root:Processing batch 31/398
INFO:root:Processing batch 32/398
INFO:root:Processing batch 33/398
INFO:root:Processing batch 34/398
INFO:root:Processing batch 35/398
INFO:root:Processing batch 36/398
INFO:root:Processing batch 37/398
INFO:root:Processing batch 38/398
INFO:root:Processing batch 39/398
INFO:root:Processing batch 40/398
INFO:root:Processing batch 41/398
INFO:root:Processing batch 42/398
INFO:root:Processing batch 43/398
INFO:root:Processing batch 44/398
INFO:root:Processing batch 45/398
INFO:root:Processing batch 46/398
INFO:root:Processing batch 47/398
INFO:root:Processing batch 48/398
INFO:root:Processing batch 49/398
INFO:root:Processing batch 50/398
INFO:root:Processing batch 51/398
INFO:root:Processing batch 52/398
INFO:root:Processing batch 53/398
INFO:root:Processing batch 54/398
INFO:root:Processing batch 55/398
INFO:root:Processing batch 56/398
INFO:root:Processing batch 57/398
INFO:root:Processing batch 58/398
INFO:root:Processing batch 59/398
INFO:root:Processing batch 60/398
INFO:root:Processing batch 61/398
INFO:root:Processing batch 62/398
INFO:root:Processing batch 63/398
INFO:root:Processing batch 64/398
INFO:root:Processing batch 65/398
INFO:root:Processing batch 66/398
INFO:root:Processing batch 67/398
INFO:root:Processing batch 68/398
INFO:root:Processing batch 69/398
INFO:root:Processing batch 70/398
INFO:root:Processing batch 71/398
INFO:root:Processing batch 72/398
INFO:root:Processing batch 73/398
INFO:root:Processing batch 74/398
INFO:root:Processing batch 75/398
INFO:root:Processing batch 76/398
INFO:root:Processing batch 77/398
INFO:root:Processing batch 78/398
INFO:root:Processing batch 79/398
INFO:root:Processing batch 80/398
INFO:root:Processing batch 81/398
INFO:root:Processing batch 82/398
INFO:root:Processing batch 83/398
INFO:root:Processing batch 84/398
INFO:root:Processing batch 85/398
INFO:root:Processing batch 86/398
INFO:root:Processing batch 87/398
INFO:root:Processing batch 88/398
INFO:root:Processing batch 89/398
INFO:root:Processing batch 90/398
INFO:root:Processing batch 91/398
INFO:root:Processing batch 92/398
INFO:root:Processing batch 93/398
INFO:root:Processing batch 94/398
INFO:root:Processing batch 95/398
INFO:root:Processing batch 96/398
INFO:root:Processing batch 97/398
INFO:root:Processing batch 98/398
INFO:root:Processing batch 99/398
INFO:root:Processing batch 100/398
INFO:root:Processing batch 101/398
INFO:root:Processing batch 102/398
INFO:root:Processing batch 103/398
INFO:root:Processing batch 104/398
INFO:root:Processing batch 105/398
INFO:root:Processing batch 106/398
INFO:root:Processing batch 107/398
INFO:root:Processing batch 108/398
INFO:root:Processing batch 109/398
INFO:root:Processing batch 110/398
INFO:root:Processing batch 111/398
INFO:root:Processing batch 112/398
INFO:root:Processing batch 113/398
INFO:root:Processing batch 114/398
INFO:root:Processing batch 115/398
INFO:root:Processing batch 116/398
INFO:root:Processing batch 117/398
INFO:root:Processing batch 118/398
INFO:root:Processing batch 119/398
INFO:root:Processing batch 120/398
INFO:root:Processing batch 121/398
INFO:root:Processing batch 122/398
INFO:root:Processing batch 123/398
INFO:root:Processing batch 124/398
INFO:root:Processing batch 125/398
INFO:root:Processing batch 126/398
INFO:root:Processing batch 127/398
INFO:root:Processing batch 128/398
INFO:root:Processing batch 129/398
INFO:root:Processing batch 130/398
INFO:root:Processing batch 131/398
INFO:root:Processing batch 132/398
INFO:root:Processing batch 133/398
INFO:root:Processing batch 134/398
INFO:root:Processing batch 135/398
INFO:root:Processing batch 136/398
INFO:root:Processing batch 137/398
INFO:root:Processing batch 138/398
INFO:root:Processing batch 139/398
INFO:root:Processing batch 140/398
INFO:root:Processing batch 141/398
INFO:root:Processing batch 142/398
INFO:root:Processing batch 143/398
INFO:root:Processing batch 144/398
INFO:root:Processing batch 145/398
INFO:root:Processing batch 146/398
INFO:root:Processing batch 147/398
INFO:root:Processing batch 148/398
INFO:root:Processing batch 149/398
INFO:root:Processing batch 150/398
INFO:root:Processing batch 151/398
INFO:root:Processing batch 152/398
INFO:root:Processing batch 153/398
INFO:root:Processing batch 154/398
INFO:root:Processing batch 155/398
INFO:root:Processing batch 156/398
INFO:root:Processing batch 157/398
INFO:root:Processing batch 158/398
INFO:root:Processing batch 159/398
INFO:root:Processing batch 160/398
INFO:root:Processing batch 161/398
INFO:root:Processing batch 162/398
INFO:root:Processing batch 163/398
INFO:root:Processing batch 164/398
INFO:root:Processing batch 165/398
INFO:root:Processing batch 166/398
INFO:root:Processing batch 167/398
INFO:root:Processing batch 168/398
INFO:root:Processing batch 169/398
INFO:root:Processing batch 170/398
INFO:root:Processing batch 171/398
INFO:root:Processing batch 172/398
INFO:root:Processing batch 173/398
INFO:root:Processing batch 174/398
INFO:root:Processing batch 175/398
INFO:root:Processing batch 176/398
INFO:root:Processing batch 177/398
INFO:root:Processing batch 178/398
INFO:root:Processing batch 179/398
INFO:root:Processing batch 180/398
INFO:root:Processing batch 181/398
INFO:root:Processing batch 182/398
INFO:root:Processing batch 183/398
INFO:root:Processing batch 184/398
INFO:root:Processing batch 185/398
INFO:root:Processing batch 186/398
INFO:root:Processing batch 187/398
INFO:root:Processing batch 188/398
INFO:root:Processing batch 189/398
INFO:root:Processing batch 190/398
INFO:root:Processing batch 191/398
INFO:root:Processing batch 192/398
INFO:root:Processing batch 193/398
INFO:root:Processing batch 194/398
INFO:root:Processing batch 195/398
INFO:root:Processing batch 196/398
INFO:root:Processing batch 197/398
INFO:root:Processing batch 198/398
INFO:root:Processing batch 199/398
INFO:root:Processing batch 200/398
INFO:root:Processing batch 201/398
INFO:root:Processing batch 202/398
INFO:root:Processing batch 203/398
INFO:root:Processing batch 204/398
INFO:root:Processing batch 205/398
INFO:root:Processing batch 206/398
INFO:root:Processing batch 207/398
INFO:root:Processing batch 208/398
INFO:root:Processing batch 209/398
INFO:root:Processing batch 210/398
INFO:root:Processing batch 211/398
INFO:root:Processing batch 212/398
INFO:root:Processing batch 213/398
INFO:root:Processing batch 214/398
INFO:root:Processing batch 215/398
INFO:root:Processing batch 216/398
INFO:root:Processing batch 217/398
INFO:root:Processing batch 218/398
INFO:root:Processing batch 219/398
INFO:root:Processing batch 220/398
INFO:root:Processing batch 221/398
INFO:root:Processing batch 222/398
INFO:root:Processing batch 223/398
INFO:root:Processing batch 224/398
INFO:root:Processing batch 225/398
INFO:root:Processing batch 226/398
INFO:root:Processing batch 227/398
INFO:root:Processing batch 228/398
INFO:root:Processing batch 229/398
INFO:root:Processing batch 230/398
INFO:root:Processing batch 231/398
INFO:root:Processing batch 232/398
INFO:root:Processing batch 233/398
INFO:root:Processing batch 234/398
INFO:root:Processing batch 235/398
INFO:root:Processing batch 236/398
INFO:root:Processing batch 237/398
INFO:root:Processing batch 238/398
INFO:root:Processing batch 239/398
INFO:root:Processing batch 240/398
INFO:root:Processing batch 241/398
INFO:root:Processing batch 242/398
INFO:root:Processing batch 243/398
INFO:root:Processing batch 244/398
INFO:root:Processing batch 245/398
INFO:root:Processing batch 246/398
INFO:root:Processing batch 247/398
INFO:root:Processing batch 248/398
INFO:root:Processing batch 249/398
INFO:root:Processing batch 250/398
INFO:root:Processing batch 251/398
INFO:root:Processing batch 252/398
INFO:root:Processing batch 253/398
INFO:root:Processing batch 254/398
INFO:root:Processing batch 255/398
INFO:root:Processing batch 256/398
INFO:root:Processing batch 257/398
INFO:root:Processing batch 258/398
INFO:root:Processing batch 259/398
INFO:root:Processing batch 260/398
INFO:root:Processing batch 261/398
INFO:root:Processing batch 262/398
INFO:root:Processing batch 263/398
INFO:root:Processing batch 264/398
INFO:root:Processing batch 265/398
INFO:root:Processing batch 266/398
INFO:root:Processing batch 267/398
INFO:root:Processing batch 268/398
INFO:root:Processing batch 269/398
INFO:root:Processing batch 270/398
INFO:root:Processing batch 271/398
INFO:root:Processing batch 272/398
INFO:root:Processing batch 273/398
INFO:root:Processing batch 274/398
INFO:root:Processing batch 275/398
INFO:root:Processing batch 276/398
INFO:root:Processing batch 277/398
INFO:root:Processing batch 278/398
INFO:root:Processing batch 279/398
INFO:root:Processing batch 280/398
INFO:root:Processing batch 281/398
INFO:root:Processing batch 282/398
INFO:root:Processing batch 283/398
INFO:root:Processing batch 284/398
INFO:root:Processing batch 285/398
INFO:root:Processing batch 286/398
INFO:root:Processing batch 287/398
INFO:root:Processing batch 288/398
INFO:root:Processing batch 289/398
INFO:root:Processing batch 290/398
INFO:root:Processing batch 291/398
INFO:root:Processing batch 292/398
INFO:root:Processing batch 293/398
INFO:root:Processing batch 294/398
INFO:root:Processing batch 295/398
INFO:root:Processing batch 296/398
INFO:root:Processing batch 297/398
INFO:root:Processing batch 298/398
INFO:root:Processing batch 299/398
INFO:root:Processing batch 300/398
INFO:root:Processing batch 301/398
INFO:root:Processing batch 302/398
INFO:root:Processing batch 303/398
INFO:root:Processing batch 304/398
INFO:root:Processing batch 305/398
INFO:root:Processing batch 306/398
INFO:root:Processing batch 307/398
INFO:root:Processing batch 308/398
INFO:root:Processing batch 309/398
INFO:root:Processing batch 310/398
INFO:root:Processing batch 311/398
INFO:root:Processing batch 312/398
INFO:root:Processing batch 313/398
INFO:root:Processing batch 314/398
INFO:root:Processing batch 315/398
INFO:root:Processing batch 316/398
INFO:root:Processing batch 317/398
INFO:root:Processing batch 318/398
INFO:root:Processing batch 319/398
INFO:root:Processing batch 320/398
INFO:root:Processing batch 321/398
INFO:root:Processing batch 322/398
INFO:root:Processing batch 323/398
INFO:root:Processing batch 324/398
INFO:root:Processing batch 325/398
INFO:root:Processing batch 326/398
INFO:root:Processing batch 327/398
INFO:root:Processing batch 328/398
INFO:root:Processing batch 329/398
INFO:root:Processing batch 330/398
INFO:root:Processing batch 331/398
INFO:root:Processing batch 332/398
INFO:root:Processing batch 333/398
INFO:root:Processing batch 334/398
INFO:root:Processing batch 335/398
INFO:root:Processing batch 336/398
INFO:root:Processing batch 337/398
INFO:root:Processing batch 338/398
INFO:root:Processing batch 339/398
INFO:root:Processing batch 340/398
INFO:root:Processing batch 341/398
INFO:root:Processing batch 342/398
INFO:root:Processing batch 343/398
INFO:root:Processing batch 344/398
INFO:root:Processing batch 345/398
INFO:root:Processing batch 346/398
INFO:root:Processing batch 347/398
INFO:root:Processing batch 348/398
INFO:root:Processing batch 349/398
INFO:root:Processing batch 350/398
INFO:root:Processing batch 351/398
INFO:root:Processing batch 352/398
INFO:root:Processing batch 353/398
INFO:root:Processing batch 354/398
INFO:root:Processing batch 355/398
INFO:root:Processing batch 356/398
INFO:root:Processing batch 357/398
INFO:root:Processing batch 358/398
INFO:root:Processing batch 359/398
INFO:root:Processing batch 360/398
INFO:root:Processing batch 361/398
INFO:root:Processing batch 362/398
INFO:root:Processing batch 363/398
INFO:root:Processing batch 364/398
INFO:root:Processing batch 365/398
INFO:root:Processing batch 366/398
INFO:root:Processing batch 367/398
INFO:root:Processing batch 368/398
INFO:root:Processing batch 369/398
INFO:root:Processing batch 370/398
INFO:root:Processing batch 371/398
INFO:root:Processing batch 372/398
INFO:root:Processing batch 373/398
INFO:root:Processing batch 374/398
INFO:root:Processing batch 375/398
INFO:root:Processing batch 376/398
INFO:root:Processing batch 377/398
INFO:root:Processing batch 378/398
INFO:root:Processing batch 379/398
INFO:root:Processing batch 380/398
INFO:root:Processing batch 381/398
INFO:root:Processing batch 382/398
INFO:root:Processing batch 383/398
INFO:root:Processing batch 384/398
INFO:root:Processing batch 385/398
INFO:root:Processing batch 386/398
INFO:root:Processing batch 387/398
INFO:root:Processing batch 388/398
INFO:root:Processing batch 389/398
INFO:root:Processing batch 390/398
INFO:root:Processing batch 391/398
INFO:root:Processing batch 392/398
INFO:root:Processing batch 393/398
INFO:root:Processing batch 394/398
INFO:root:Processing batch 395/398
INFO:root:Processing batch 396/398
INFO:root:Processing batch 397/398
INFO:root:Processing batch 398/398
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.4748102128505707, 0.4196726083755493, 0.3590792119503021], 'std': [0.27919745445251465, 0.27405115962028503, 0.2634221911430359], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.4748102128505707, 0.4196726083755493, 0.3590792119503021], std=[0.27919745445251465, 0.27405115962028503, 0.2634221911430359])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.12181
INFO:root:Training epoch 1, Iteration 20, Loss: 5.02060
INFO:root:Training epoch 1, Iteration 40, Loss: 4.85412
INFO:root:Training epoch 1, Iteration 60, Loss: 4.70104
INFO:root:Training epoch 1, Iteration 80, Loss: 4.73047
INFO:root:Training epoch 1, Iteration 100, Loss: 4.70259
INFO:root:Training epoch 1, Iteration 120, Loss: 4.62085
INFO:root:Training epoch 1, Iteration 140, Loss: 4.44954
INFO:root:Training epoch 1, Iteration 160, Loss: 4.49375
INFO:root:Training epoch 1, Iteration 180, Loss: 4.50556
INFO:root:Training epoch 1, Iteration 200, Loss: 4.43162
INFO:root:Training epoch 1, Iteration 220, Loss: 4.37833
INFO:root:Training epoch 1, Iteration 240, Loss: 4.33866
INFO:root:Training epoch 1, Iteration 260, Loss: 4.34328
INFO:root:Training epoch 1, Iteration 280, Loss: 4.26671
INFO:root:Training epoch 1, Iteration 300, Loss: 4.19448
INFO:root:Training epoch 1, Iteration 320, Loss: 4.28215
INFO:root:Training epoch 1, Iteration 340, Loss: 4.21621
INFO:root:Training epoch 1, Iteration 360, Loss: 4.19455
INFO:root:Training epoch 1, Iteration 380, Loss: 4.18966
INFO:root:Validation iteration 1, Loss: 4.48065
INFO:root:Validation iteration 8, Loss: 4.24114
INFO:root:Validation iteration 16, Loss: 4.18637
INFO:root:Validation iteration 24, Loss: 4.26884
INFO:root:Validation iteration 32, Loss: 4.27248
INFO:root:Validation iteration 40, Loss: 4.14462
INFO:root:Validation iteration 48, Loss: 4.18178
INFO:root:Validation iteration 56, Loss: 4.08260
INFO:root:Validation iteration 64, Loss: 4.05621
INFO:root:Validation iteration 72, Loss: 4.35225
INFO:root:Validation iteration 80, Loss: 4.21388
INFO:root:Validation iteration 88, Loss: 4.31909
INFO:root:Validation iteration 96, Loss: 4.06321
INFO:root:Validation iteration 104, Loss: 4.10485
INFO:root:Validation iteration 112, Loss: 4.19278
INFO:root:Validation iteration 120, Loss: 4.26429
INFO:root:Validation iteration 128, Loss: 4.24022
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.460
INFO:root:Validation accuracy: 0.072, Validation loss: 4.20233
INFO:root:Training epoch 2, Iteration 1, Loss: 4.06401
INFO:root:Training epoch 2, Iteration 20, Loss: 4.05580
INFO:root:Training epoch 2, Iteration 40, Loss: 4.07739
INFO:root:Training epoch 2, Iteration 60, Loss: 4.12302
INFO:root:Training epoch 2, Iteration 80, Loss: 4.00287
INFO:root:Training epoch 2, Iteration 100, Loss: 3.91961
INFO:root:Training epoch 2, Iteration 120, Loss: 4.03218
INFO:root:Training epoch 2, Iteration 140, Loss: 3.99887
INFO:root:Training epoch 2, Iteration 160, Loss: 3.98594
INFO:root:Training epoch 2, Iteration 180, Loss: 4.01653
INFO:root:Training epoch 2, Iteration 200, Loss: 3.98042
INFO:root:Training epoch 2, Iteration 220, Loss: 3.96600
INFO:root:Training epoch 2, Iteration 240, Loss: 3.97459
INFO:root:Training epoch 2, Iteration 260, Loss: 3.88774
INFO:root:Training epoch 2, Iteration 280, Loss: 3.92279
INFO:root:Training epoch 2, Iteration 300, Loss: 3.93115
INFO:root:Training epoch 2, Iteration 320, Loss: 3.95777
INFO:root:Training epoch 2, Iteration 340, Loss: 3.93897
INFO:root:Training epoch 2, Iteration 360, Loss: 3.88314
INFO:root:Training epoch 2, Iteration 380, Loss: 3.89512
INFO:root:Validation iteration 1, Loss: 4.10443
INFO:root:Validation iteration 8, Loss: 4.05004
INFO:root:Validation iteration 16, Loss: 3.75376
INFO:root:Validation iteration 24, Loss: 3.97459
INFO:root:Validation iteration 32, Loss: 3.94545
INFO:root:Validation iteration 40, Loss: 3.93552
INFO:root:Validation iteration 48, Loss: 3.96574
INFO:root:Validation iteration 56, Loss: 3.96462
INFO:root:Validation iteration 64, Loss: 3.94009
INFO:root:Validation iteration 72, Loss: 3.99129
INFO:root:Validation iteration 80, Loss: 3.94816
INFO:root:Validation iteration 88, Loss: 3.98989
INFO:root:Validation iteration 96, Loss: 3.85074
INFO:root:Validation iteration 104, Loss: 3.87998
INFO:root:Validation iteration 112, Loss: 4.06598
INFO:root:Validation iteration 120, Loss: 3.93924
INFO:root:Validation iteration 128, Loss: 3.95363
INFO:root:End of Epoch 2
INFO:root:Training loss: 3.969
INFO:root:Validation accuracy: 0.109, Validation loss: 3.95526
INFO:root:Training epoch 3, Iteration 1, Loss: 3.70348
INFO:root:Training epoch 3, Iteration 20, Loss: 3.68382
INFO:root:Training epoch 3, Iteration 40, Loss: 3.70016
INFO:root:Training epoch 3, Iteration 60, Loss: 3.71894
INFO:root:Training epoch 3, Iteration 80, Loss: 3.73353
INFO:root:Training epoch 3, Iteration 100, Loss: 3.82627
INFO:root:Training epoch 3, Iteration 120, Loss: 3.60757
INFO:root:Training epoch 3, Iteration 140, Loss: 3.70472
INFO:root:Training epoch 3, Iteration 160, Loss: 3.78943
INFO:root:Training epoch 3, Iteration 180, Loss: 3.64003
INFO:root:Training epoch 3, Iteration 200, Loss: 3.71938
INFO:root:Training epoch 3, Iteration 220, Loss: 3.68919
INFO:root:Training epoch 3, Iteration 240, Loss: 3.77684
INFO:root:Training epoch 3, Iteration 260, Loss: 3.67529
INFO:root:Training epoch 3, Iteration 280, Loss: 3.74131
INFO:root:Training epoch 3, Iteration 300, Loss: 3.67915
INFO:root:Training epoch 3, Iteration 320, Loss: 3.73248
INFO:root:Training epoch 3, Iteration 340, Loss: 3.72757
INFO:root:Training epoch 3, Iteration 360, Loss: 3.62142
INFO:root:Training epoch 3, Iteration 380, Loss: 3.64276
INFO:root:Validation iteration 1, Loss: 4.01272
INFO:root:Validation iteration 8, Loss: 3.79114
INFO:root:Validation iteration 16, Loss: 3.59628
INFO:root:Validation iteration 24, Loss: 3.64320
INFO:root:Validation iteration 32, Loss: 3.71835
INFO:root:Validation iteration 40, Loss: 3.73657
INFO:root:Validation iteration 48, Loss: 3.66604
INFO:root:Validation iteration 56, Loss: 3.74870
INFO:root:Validation iteration 64, Loss: 3.68379
INFO:root:Validation iteration 72, Loss: 3.84241
INFO:root:Validation iteration 80, Loss: 3.69967
INFO:root:Validation iteration 88, Loss: 3.81370
INFO:root:Validation iteration 96, Loss: 3.59281
INFO:root:Validation iteration 104, Loss: 3.64036
INFO:root:Validation iteration 112, Loss: 3.80907
INFO:root:Validation iteration 120, Loss: 3.69662
INFO:root:Validation iteration 128, Loss: 3.69782
INFO:root:End of Epoch 3
INFO:root:Training loss: 3.708
INFO:root:Validation accuracy: 0.149, Validation loss: 3.71344
INFO:root:Training epoch 4, Iteration 1, Loss: 3.29531
INFO:root:Training epoch 4, Iteration 20, Loss: 3.55413
INFO:root:Training epoch 4, Iteration 40, Loss: 3.55295
INFO:root:Training epoch 4, Iteration 60, Loss: 3.56061
INFO:root:Training epoch 4, Iteration 80, Loss: 3.47608
INFO:root:Training epoch 4, Iteration 100, Loss: 3.64515
INFO:root:Training epoch 4, Iteration 120, Loss: 3.58779
INFO:root:Training epoch 4, Iteration 140, Loss: 3.53279
INFO:root:Training epoch 4, Iteration 160, Loss: 3.47264
INFO:root:Training epoch 4, Iteration 180, Loss: 3.49249
INFO:root:Training epoch 4, Iteration 200, Loss: 3.50475
INFO:root:Training epoch 4, Iteration 220, Loss: 3.61343
INFO:root:Training epoch 4, Iteration 240, Loss: 3.48697
INFO:root:Training epoch 4, Iteration 260, Loss: 3.49139
INFO:root:Training epoch 4, Iteration 280, Loss: 3.40146
INFO:root:Training epoch 4, Iteration 300, Loss: 3.40042
INFO:root:Training epoch 4, Iteration 320, Loss: 3.47857
INFO:root:Training epoch 4, Iteration 340, Loss: 3.45195
INFO:root:Training epoch 4, Iteration 360, Loss: 3.48749
INFO:root:Training epoch 4, Iteration 380, Loss: 3.38974
INFO:root:Validation iteration 1, Loss: 3.90335
INFO:root:Validation iteration 8, Loss: 3.80348
INFO:root:Validation iteration 16, Loss: 3.44178
INFO:root:Validation iteration 24, Loss: 3.57742
INFO:root:Validation iteration 32, Loss: 3.58064
INFO:root:Validation iteration 40, Loss: 3.60620
INFO:root:Validation iteration 48, Loss: 3.54988
INFO:root:Validation iteration 56, Loss: 3.65205
INFO:root:Validation iteration 64, Loss: 3.53287
INFO:root:Validation iteration 72, Loss: 3.60419
INFO:root:Validation iteration 80, Loss: 3.55760
INFO:root:Validation iteration 88, Loss: 3.64020
INFO:root:Validation iteration 96, Loss: 3.43202
INFO:root:Validation iteration 104, Loss: 3.39881
INFO:root:Validation iteration 112, Loss: 3.59482
INFO:root:Validation iteration 120, Loss: 3.57035
INFO:root:Validation iteration 128, Loss: 3.52649
INFO:root:End of Epoch 4
INFO:root:Training loss: 3.499
INFO:root:Validation accuracy: 0.179, Validation loss: 3.57490
INFO:root:Training epoch 5, Iteration 1, Loss: 3.40911
INFO:root:Training epoch 5, Iteration 20, Loss: 3.27510
INFO:root:Training epoch 5, Iteration 40, Loss: 3.37312
INFO:root:Training epoch 5, Iteration 60, Loss: 3.31038
INFO:root:Training epoch 5, Iteration 80, Loss: 3.39167
INFO:root:Training epoch 5, Iteration 100, Loss: 3.33676
INFO:root:Training epoch 5, Iteration 120, Loss: 3.33500
INFO:root:Training epoch 5, Iteration 140, Loss: 3.30472
INFO:root:Training epoch 5, Iteration 160, Loss: 3.26986
INFO:root:Training epoch 5, Iteration 180, Loss: 3.33907
INFO:root:Training epoch 5, Iteration 200, Loss: 3.27603
INFO:root:Training epoch 5, Iteration 220, Loss: 3.48624
INFO:root:Training epoch 5, Iteration 240, Loss: 3.28934
INFO:root:Training epoch 5, Iteration 260, Loss: 3.39373
INFO:root:Training epoch 5, Iteration 280, Loss: 3.31631
INFO:root:Training epoch 5, Iteration 300, Loss: 3.38033
INFO:root:Training epoch 5, Iteration 320, Loss: 3.35744
INFO:root:Training epoch 5, Iteration 340, Loss: 3.40628
INFO:root:Training epoch 5, Iteration 360, Loss: 3.33203
INFO:root:Training epoch 5, Iteration 380, Loss: 3.23218
INFO:root:Validation iteration 1, Loss: 4.06748
INFO:root:Validation iteration 8, Loss: 3.65564
INFO:root:Validation iteration 16, Loss: 3.35551
INFO:root:Validation iteration 24, Loss: 3.51527
INFO:root:Validation iteration 32, Loss: 3.37329
INFO:root:Validation iteration 40, Loss: 3.53927
INFO:root:Validation iteration 48, Loss: 3.49397
INFO:root:Validation iteration 56, Loss: 3.53725
INFO:root:Validation iteration 64, Loss: 3.36141
INFO:root:Validation iteration 72, Loss: 3.63184
INFO:root:Validation iteration 80, Loss: 3.40443
INFO:root:Validation iteration 88, Loss: 3.52146
INFO:root:Validation iteration 96, Loss: 3.35329
INFO:root:Validation iteration 104, Loss: 3.36781
INFO:root:Validation iteration 112, Loss: 3.54299
INFO:root:Validation iteration 120, Loss: 3.51656
INFO:root:Validation iteration 128, Loss: 3.51430
INFO:root:End of Epoch 5
INFO:root:Training loss: 3.339
INFO:root:Validation accuracy: 0.196, Validation loss: 3.48732
INFO:root:Training epoch 6, Iteration 1, Loss: 3.14891
INFO:root:Training epoch 6, Iteration 20, Loss: 3.20325
INFO:root:Training epoch 6, Iteration 40, Loss: 3.32514
INFO:root:Training epoch 6, Iteration 60, Loss: 3.27989
INFO:root:Training epoch 6, Iteration 80, Loss: 3.24472
INFO:root:Training epoch 6, Iteration 100, Loss: 3.06446
INFO:root:Training epoch 6, Iteration 120, Loss: 3.16382
INFO:root:Training epoch 6, Iteration 140, Loss: 3.18157
INFO:root:Training epoch 6, Iteration 160, Loss: 3.11286
INFO:root:Training epoch 6, Iteration 180, Loss: 3.26710
INFO:root:Training epoch 6, Iteration 200, Loss: 3.29779
INFO:root:Training epoch 6, Iteration 220, Loss: 3.23273
INFO:root:Training epoch 6, Iteration 240, Loss: 3.16430
INFO:root:Training epoch 6, Iteration 260, Loss: 3.07782
INFO:root:Training epoch 6, Iteration 280, Loss: 3.22984
INFO:root:Training epoch 6, Iteration 300, Loss: 3.30028
INFO:root:Training epoch 6, Iteration 320, Loss: 3.21437
INFO:root:Training epoch 6, Iteration 340, Loss: 3.19390
INFO:root:Training epoch 6, Iteration 360, Loss: 3.10893
INFO:root:Training epoch 6, Iteration 380, Loss: 3.20377
INFO:root:Validation iteration 1, Loss: 3.63584
INFO:root:Validation iteration 8, Loss: 3.55849
INFO:root:Validation iteration 16, Loss: 3.29821
INFO:root:Validation iteration 24, Loss: 3.53772
INFO:root:Validation iteration 32, Loss: 3.42888
INFO:root:Validation iteration 40, Loss: 3.43712
INFO:root:Validation iteration 48, Loss: 3.43477
INFO:root:Validation iteration 56, Loss: 3.47367
INFO:root:Validation iteration 64, Loss: 3.28702
INFO:root:Validation iteration 72, Loss: 3.66950
INFO:root:Validation iteration 80, Loss: 3.38475
INFO:root:Validation iteration 88, Loss: 3.45588
INFO:root:Validation iteration 96, Loss: 3.44788
INFO:root:Validation iteration 104, Loss: 3.24262
INFO:root:Validation iteration 112, Loss: 3.51766
INFO:root:Validation iteration 120, Loss: 3.42577
INFO:root:Validation iteration 128, Loss: 3.31173
INFO:root:End of Epoch 6
INFO:root:Training loss: 3.203
INFO:root:Validation accuracy: 0.211, Validation loss: 3.43781
INFO:root:Best validation accuracy: 0.211 at epoch 6
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.39943
INFO:root:Validation iteration 8, Loss: 3.64617
INFO:root:Validation iteration 16, Loss: 3.52583
INFO:root:Validation iteration 24, Loss: 3.54796
INFO:root:Validation iteration 32, Loss: 3.37326
INFO:root:Validation iteration 40, Loss: 3.50051
INFO:root:Validation iteration 48, Loss: 3.40266
INFO:root:Validation iteration 56, Loss: 3.24070
INFO:root:Validation iteration 64, Loss: 3.20024
INFO:root:Validation iteration 72, Loss: 3.26308
INFO:root:Validation iteration 80, Loss: 3.13849
INFO:root:Validation iteration 88, Loss: 3.45928
INFO:root:Validation iteration 96, Loss: 3.22747
INFO:root:Validation iteration 104, Loss: 3.44451
INFO:root:Validation iteration 112, Loss: 3.47266
INFO:root:Validation iteration 120, Loss: 3.44653
INFO:root:Validation iteration 128, Loss: 3.39082
Test accuracy: 0.224, Test loss: 3.39625
INFO:root:Saving results...
INFO:root:Done!
"""

string19 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', test_root='./data/kaggle_testset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.', trained_model_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/temp/best_model_5.pth', predictions_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/predictions.csv'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size_model=32, batch_size_stats=128, train_split_size=0.75), 'train': TrainConfig(num_epochs=6, train_log_frequency=20, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=1e-05, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False, save_predictions=False, resume_training=True), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/100
INFO:root:Processing batch 2/100
INFO:root:Processing batch 3/100
INFO:root:Processing batch 4/100
INFO:root:Processing batch 5/100
INFO:root:Processing batch 6/100
INFO:root:Processing batch 7/100
INFO:root:Processing batch 8/100
INFO:root:Processing batch 9/100
INFO:root:Processing batch 10/100
INFO:root:Processing batch 11/100
INFO:root:Processing batch 12/100
INFO:root:Processing batch 13/100
INFO:root:Processing batch 14/100
INFO:root:Processing batch 15/100
INFO:root:Processing batch 16/100
INFO:root:Processing batch 17/100
INFO:root:Processing batch 18/100
INFO:root:Processing batch 19/100
INFO:root:Processing batch 20/100
INFO:root:Processing batch 21/100
INFO:root:Processing batch 22/100
INFO:root:Processing batch 23/100
INFO:root:Processing batch 24/100
INFO:root:Processing batch 25/100
INFO:root:Processing batch 26/100
INFO:root:Processing batch 27/100
INFO:root:Processing batch 28/100
INFO:root:Processing batch 29/100
INFO:root:Processing batch 30/100
INFO:root:Processing batch 31/100
INFO:root:Processing batch 32/100
INFO:root:Processing batch 33/100
INFO:root:Processing batch 34/100
INFO:root:Processing batch 35/100
INFO:root:Processing batch 36/100
INFO:root:Processing batch 37/100
INFO:root:Processing batch 38/100
INFO:root:Processing batch 39/100
INFO:root:Processing batch 40/100
INFO:root:Processing batch 41/100
INFO:root:Processing batch 42/100
INFO:root:Processing batch 43/100
INFO:root:Processing batch 44/100
INFO:root:Processing batch 45/100
INFO:root:Processing batch 46/100
INFO:root:Processing batch 47/100
INFO:root:Processing batch 48/100
INFO:root:Processing batch 49/100
INFO:root:Processing batch 50/100
INFO:root:Processing batch 51/100
INFO:root:Processing batch 52/100
INFO:root:Processing batch 53/100
INFO:root:Processing batch 54/100
INFO:root:Processing batch 55/100
INFO:root:Processing batch 56/100
INFO:root:Processing batch 57/100
INFO:root:Processing batch 58/100
INFO:root:Processing batch 59/100
INFO:root:Processing batch 60/100
INFO:root:Processing batch 61/100
INFO:root:Processing batch 62/100
INFO:root:Processing batch 63/100
INFO:root:Processing batch 64/100
INFO:root:Processing batch 65/100
INFO:root:Processing batch 66/100
INFO:root:Processing batch 67/100
INFO:root:Processing batch 68/100
INFO:root:Processing batch 69/100
INFO:root:Processing batch 70/100
INFO:root:Processing batch 71/100
INFO:root:Processing batch 72/100
INFO:root:Processing batch 73/100
INFO:root:Processing batch 74/100
INFO:root:Processing batch 75/100
INFO:root:Processing batch 76/100
INFO:root:Processing batch 77/100
INFO:root:Processing batch 78/100
INFO:root:Processing batch 79/100
INFO:root:Processing batch 80/100
INFO:root:Processing batch 81/100
INFO:root:Processing batch 82/100
INFO:root:Processing batch 83/100
INFO:root:Processing batch 84/100
INFO:root:Processing batch 85/100
INFO:root:Processing batch 86/100
INFO:root:Processing batch 87/100
INFO:root:Processing batch 88/100
INFO:root:Processing batch 89/100
INFO:root:Processing batch 90/100
INFO:root:Processing batch 91/100
INFO:root:Processing batch 92/100
INFO:root:Processing batch 93/100
INFO:root:Processing batch 94/100
INFO:root:Processing batch 95/100
INFO:root:Processing batch 96/100
INFO:root:Processing batch 97/100
INFO:root:Processing batch 98/100
INFO:root:Processing batch 99/100
INFO:root:Processing batch 100/100
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47481051087379456, 0.4196726083755493, 0.3590790629386902], 'std': [0.27919673919677734, 0.27405110001564026, 0.2634223699569702], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47481051087379456, 0.4196726083755493, 0.3590790629386902], std=[0.27919673919677734, 0.27405110001564026, 0.2634223699569702])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 3.50093
INFO:root:Training epoch 1, Iteration 20, Loss: 3.18304
INFO:root:Training epoch 1, Iteration 40, Loss: 2.98998
INFO:root:Training epoch 1, Iteration 60, Loss: 3.16731
INFO:root:Training epoch 1, Iteration 80, Loss: 3.08379
INFO:root:Training epoch 1, Iteration 100, Loss: 3.16147
INFO:root:Training epoch 1, Iteration 120, Loss: 2.95688
INFO:root:Training epoch 1, Iteration 140, Loss: 3.28879
INFO:root:Training epoch 1, Iteration 160, Loss: 3.00338
INFO:root:Training epoch 1, Iteration 180, Loss: 3.05357
INFO:root:Training epoch 1, Iteration 200, Loss: 3.09506
INFO:root:Training epoch 1, Iteration 220, Loss: 3.03182
INFO:root:Training epoch 1, Iteration 240, Loss: 3.08240
INFO:root:Training epoch 1, Iteration 260, Loss: 3.05930
INFO:root:Training epoch 1, Iteration 280, Loss: 3.05272
INFO:root:Training epoch 1, Iteration 300, Loss: 2.88079
INFO:root:Training epoch 1, Iteration 320, Loss: 3.01921
INFO:root:Training epoch 1, Iteration 340, Loss: 3.03148
INFO:root:Training epoch 1, Iteration 360, Loss: 3.04696
INFO:root:Training epoch 1, Iteration 380, Loss: 2.91248
INFO:root:Validation iteration 1, Loss: 3.56912
INFO:root:Validation iteration 8, Loss: 3.39112
INFO:root:Validation iteration 16, Loss: 3.12526
INFO:root:Validation iteration 24, Loss: 3.29027
INFO:root:Validation iteration 32, Loss: 3.08920
INFO:root:Validation iteration 40, Loss: 3.26569
INFO:root:Validation iteration 48, Loss: 3.25986
INFO:root:Validation iteration 56, Loss: 3.26392
INFO:root:Validation iteration 64, Loss: 3.10383
INFO:root:Validation iteration 72, Loss: 3.38937
INFO:root:Validation iteration 80, Loss: 3.17580
INFO:root:Validation iteration 88, Loss: 3.24312
INFO:root:Validation iteration 96, Loss: 3.13991
INFO:root:Validation iteration 104, Loss: 3.10742
INFO:root:Validation iteration 112, Loss: 3.36343
INFO:root:Validation iteration 120, Loss: 3.24960
INFO:root:Validation iteration 128, Loss: 3.22108
INFO:root:End of Epoch 1
INFO:root:Training loss: 3.055
INFO:root:Validation accuracy: 0.240, Validation loss: 3.23805
INFO:root:Training epoch 2, Iteration 1, Loss: 2.76210
INFO:root:Training epoch 2, Iteration 20, Loss: 3.00407
INFO:root:Training epoch 2, Iteration 40, Loss: 3.02398
INFO:root:Training epoch 2, Iteration 60, Loss: 2.97044
INFO:root:Training epoch 2, Iteration 80, Loss: 2.94090
INFO:root:Training epoch 2, Iteration 100, Loss: 3.03184
INFO:root:Training epoch 2, Iteration 120, Loss: 2.99553
INFO:root:Training epoch 2, Iteration 140, Loss: 2.96196
INFO:root:Training epoch 2, Iteration 160, Loss: 2.94649
INFO:root:Training epoch 2, Iteration 180, Loss: 2.89405
INFO:root:Training epoch 2, Iteration 200, Loss: 3.02248
INFO:root:Training epoch 2, Iteration 220, Loss: 2.87278
INFO:root:Training epoch 2, Iteration 240, Loss: 2.97864
INFO:root:Training epoch 2, Iteration 260, Loss: 2.88478
INFO:root:Training epoch 2, Iteration 280, Loss: 2.88400
INFO:root:Training epoch 2, Iteration 300, Loss: 3.02379
INFO:root:Training epoch 2, Iteration 320, Loss: 2.87532
INFO:root:Training epoch 2, Iteration 340, Loss: 3.01894
INFO:root:Training epoch 2, Iteration 360, Loss: 3.03053
INFO:root:Training epoch 2, Iteration 380, Loss: 2.89460
INFO:root:Validation iteration 1, Loss: 3.52198
INFO:root:Validation iteration 8, Loss: 3.37060
INFO:root:Validation iteration 16, Loss: 3.06214
INFO:root:Validation iteration 24, Loss: 3.19614
INFO:root:Validation iteration 32, Loss: 3.12793
INFO:root:Validation iteration 40, Loss: 3.28009
INFO:root:Validation iteration 48, Loss: 3.20879
INFO:root:Validation iteration 56, Loss: 3.25033
INFO:root:Validation iteration 64, Loss: 3.08450
INFO:root:Validation iteration 72, Loss: 3.31973
INFO:root:Validation iteration 80, Loss: 3.15388
INFO:root:Validation iteration 88, Loss: 3.21166
INFO:root:Validation iteration 96, Loss: 3.11830
INFO:root:Validation iteration 104, Loss: 3.03141
INFO:root:Validation iteration 112, Loss: 3.31146
INFO:root:Validation iteration 120, Loss: 3.19318
INFO:root:Validation iteration 128, Loss: 3.18888
INFO:root:End of Epoch 2
INFO:root:Training loss: 2.961
INFO:root:Validation accuracy: 0.243, Validation loss: 3.20150
INFO:root:Training epoch 3, Iteration 1, Loss: 2.24309
INFO:root:Training epoch 3, Iteration 20, Loss: 2.86613
INFO:root:Training epoch 3, Iteration 40, Loss: 3.02666
INFO:root:Training epoch 3, Iteration 60, Loss: 2.85510
INFO:root:Training epoch 3, Iteration 80, Loss: 2.87613
INFO:root:Training epoch 3, Iteration 100, Loss: 2.94179
INFO:root:Training epoch 3, Iteration 120, Loss: 2.81617
INFO:root:Training epoch 3, Iteration 140, Loss: 2.84044
INFO:root:Training epoch 3, Iteration 160, Loss: 2.96340
INFO:root:Training epoch 3, Iteration 180, Loss: 2.83625
INFO:root:Training epoch 3, Iteration 200, Loss: 3.00667
INFO:root:Training epoch 3, Iteration 220, Loss: 3.00672
INFO:root:Training epoch 3, Iteration 240, Loss: 2.94558
INFO:root:Training epoch 3, Iteration 260, Loss: 2.88173
INFO:root:Training epoch 3, Iteration 280, Loss: 2.74254
INFO:root:Training epoch 3, Iteration 300, Loss: 2.87323
INFO:root:Training epoch 3, Iteration 320, Loss: 2.98155
INFO:root:Training epoch 3, Iteration 340, Loss: 2.87347
INFO:root:Training epoch 3, Iteration 360, Loss: 2.94271
INFO:root:Training epoch 3, Iteration 380, Loss: 2.99994
INFO:root:Validation iteration 1, Loss: 3.52982
INFO:root:Validation iteration 8, Loss: 3.36503
INFO:root:Validation iteration 16, Loss: 3.06092
INFO:root:Validation iteration 24, Loss: 3.17286
INFO:root:Validation iteration 32, Loss: 3.14273
INFO:root:Validation iteration 40, Loss: 3.25294
INFO:root:Validation iteration 48, Loss: 3.19353
INFO:root:Validation iteration 56, Loss: 3.20556
INFO:root:Validation iteration 64, Loss: 3.05922
INFO:root:Validation iteration 72, Loss: 3.32529
INFO:root:Validation iteration 80, Loss: 3.12356
INFO:root:Validation iteration 88, Loss: 3.17289
INFO:root:Validation iteration 96, Loss: 3.06702
INFO:root:Validation iteration 104, Loss: 2.96681
INFO:root:Validation iteration 112, Loss: 3.26414
INFO:root:Validation iteration 120, Loss: 3.12282
INFO:root:Validation iteration 128, Loss: 3.14591
INFO:root:End of Epoch 3
INFO:root:Training loss: 2.911
INFO:root:Validation accuracy: 0.251, Validation loss: 3.17285
INFO:root:Training epoch 4, Iteration 1, Loss: 3.00449
INFO:root:Training epoch 4, Iteration 20, Loss: 2.88507
INFO:root:Training epoch 4, Iteration 40, Loss: 2.85058
INFO:root:Training epoch 4, Iteration 60, Loss: 2.86729
INFO:root:Training epoch 4, Iteration 80, Loss: 2.77732
INFO:root:Training epoch 4, Iteration 100, Loss: 2.86549
INFO:root:Training epoch 4, Iteration 120, Loss: 2.83437
INFO:root:Training epoch 4, Iteration 140, Loss: 2.79532
INFO:root:Training epoch 4, Iteration 160, Loss: 2.81497
INFO:root:Training epoch 4, Iteration 180, Loss: 2.80415
INFO:root:Training epoch 4, Iteration 200, Loss: 3.05841
INFO:root:Training epoch 4, Iteration 220, Loss: 2.96911
INFO:root:Training epoch 4, Iteration 240, Loss: 2.87118
INFO:root:Training epoch 4, Iteration 260, Loss: 2.75033
INFO:root:Training epoch 4, Iteration 280, Loss: 2.91824
INFO:root:Training epoch 4, Iteration 300, Loss: 2.88985
INFO:root:Training epoch 4, Iteration 320, Loss: 2.97057
INFO:root:Training epoch 4, Iteration 340, Loss: 2.91758
INFO:root:Training epoch 4, Iteration 360, Loss: 2.89459
INFO:root:Training epoch 4, Iteration 380, Loss: 2.82746
INFO:root:Validation iteration 1, Loss: 3.53178
INFO:root:Validation iteration 8, Loss: 3.34741
INFO:root:Validation iteration 16, Loss: 3.03837
INFO:root:Validation iteration 24, Loss: 3.13444
INFO:root:Validation iteration 32, Loss: 3.06217
INFO:root:Validation iteration 40, Loss: 3.20520
INFO:root:Validation iteration 48, Loss: 3.19210
INFO:root:Validation iteration 56, Loss: 3.14683
INFO:root:Validation iteration 64, Loss: 3.07277
INFO:root:Validation iteration 72, Loss: 3.29252
INFO:root:Validation iteration 80, Loss: 3.08735
INFO:root:Validation iteration 88, Loss: 3.14468
INFO:root:Validation iteration 96, Loss: 3.09694
INFO:root:Validation iteration 104, Loss: 2.99783
INFO:root:Validation iteration 112, Loss: 3.21079
INFO:root:Validation iteration 120, Loss: 3.12165
INFO:root:Validation iteration 128, Loss: 3.10402
INFO:root:End of Epoch 4
INFO:root:Training loss: 2.874
INFO:root:Validation accuracy: 0.255, Validation loss: 3.14879
INFO:root:Training epoch 5, Iteration 1, Loss: 2.44512
INFO:root:Training epoch 5, Iteration 20, Loss: 2.85043
INFO:root:Training epoch 5, Iteration 40, Loss: 2.86542
INFO:root:Training epoch 5, Iteration 60, Loss: 2.91231
INFO:root:Training epoch 5, Iteration 80, Loss: 2.86013
INFO:root:Training epoch 5, Iteration 100, Loss: 2.87456
INFO:root:Training epoch 5, Iteration 120, Loss: 2.74984
INFO:root:Training epoch 5, Iteration 140, Loss: 2.80686
INFO:root:Training epoch 5, Iteration 160, Loss: 2.88553
INFO:root:Training epoch 5, Iteration 180, Loss: 2.81675
INFO:root:Training epoch 5, Iteration 200, Loss: 2.93325
INFO:root:Training epoch 5, Iteration 220, Loss: 2.83990
INFO:root:Training epoch 5, Iteration 240, Loss: 2.92768
INFO:root:Training epoch 5, Iteration 260, Loss: 2.90840
INFO:root:Training epoch 5, Iteration 280, Loss: 2.84588
INFO:root:Training epoch 5, Iteration 300, Loss: 2.76744
INFO:root:Training epoch 5, Iteration 320, Loss: 2.93801
INFO:root:Training epoch 5, Iteration 340, Loss: 2.72428
INFO:root:Training epoch 5, Iteration 360, Loss: 2.78392
INFO:root:Training epoch 5, Iteration 380, Loss: 2.71816
INFO:root:Validation iteration 1, Loss: 3.50120
INFO:root:Validation iteration 8, Loss: 3.28367
INFO:root:Validation iteration 16, Loss: 3.01305
INFO:root:Validation iteration 24, Loss: 3.13452
INFO:root:Validation iteration 32, Loss: 3.01898
INFO:root:Validation iteration 40, Loss: 3.17825
INFO:root:Validation iteration 48, Loss: 3.16577
INFO:root:Validation iteration 56, Loss: 3.14397
INFO:root:Validation iteration 64, Loss: 3.05317
INFO:root:Validation iteration 72, Loss: 3.22827
INFO:root:Validation iteration 80, Loss: 3.08537
INFO:root:Validation iteration 88, Loss: 3.09135
INFO:root:Validation iteration 96, Loss: 3.03008
INFO:root:Validation iteration 104, Loss: 2.94980
INFO:root:Validation iteration 112, Loss: 3.20556
INFO:root:Validation iteration 120, Loss: 3.12891
INFO:root:Validation iteration 128, Loss: 3.14711
INFO:root:End of Epoch 5
INFO:root:Training loss: 2.844
INFO:root:Validation accuracy: 0.257, Validation loss: 3.12519
INFO:root:Training epoch 6, Iteration 1, Loss: 2.91372
INFO:root:Training epoch 6, Iteration 20, Loss: 2.80052
INFO:root:Training epoch 6, Iteration 40, Loss: 2.70365
INFO:root:Training epoch 6, Iteration 60, Loss: 2.88201
INFO:root:Training epoch 6, Iteration 80, Loss: 2.87299
INFO:root:Training epoch 6, Iteration 100, Loss: 2.77189
INFO:root:Training epoch 6, Iteration 120, Loss: 2.70526
INFO:root:Training epoch 6, Iteration 140, Loss: 2.71294
INFO:root:Training epoch 6, Iteration 160, Loss: 2.85033
INFO:root:Training epoch 6, Iteration 180, Loss: 2.69368
INFO:root:Training epoch 6, Iteration 200, Loss: 2.78561
INFO:root:Training epoch 6, Iteration 220, Loss: 2.84962
INFO:root:Training epoch 6, Iteration 240, Loss: 2.83609
INFO:root:Training epoch 6, Iteration 260, Loss: 2.72996
INFO:root:Training epoch 6, Iteration 280, Loss: 2.82553
INFO:root:Training epoch 6, Iteration 300, Loss: 2.85564
INFO:root:Training epoch 6, Iteration 320, Loss: 2.75325
INFO:root:Training epoch 6, Iteration 340, Loss: 2.81630
INFO:root:Training epoch 6, Iteration 360, Loss: 2.75962
INFO:root:Training epoch 6, Iteration 380, Loss: 2.87026
INFO:root:Validation iteration 1, Loss: 3.48970
INFO:root:Validation iteration 8, Loss: 3.33815
INFO:root:Validation iteration 16, Loss: 2.99386
INFO:root:Validation iteration 24, Loss: 3.12000
INFO:root:Validation iteration 32, Loss: 3.01702
INFO:root:Validation iteration 40, Loss: 3.15947
INFO:root:Validation iteration 48, Loss: 3.16845
INFO:root:Validation iteration 56, Loss: 3.09039
INFO:root:Validation iteration 64, Loss: 2.98308
INFO:root:Validation iteration 72, Loss: 3.24325
INFO:root:Validation iteration 80, Loss: 3.06659
INFO:root:Validation iteration 88, Loss: 3.09855
INFO:root:Validation iteration 96, Loss: 3.01573
INFO:root:Validation iteration 104, Loss: 2.90705
INFO:root:Validation iteration 112, Loss: 3.20666
INFO:root:Validation iteration 120, Loss: 3.09887
INFO:root:Validation iteration 128, Loss: 3.01241
INFO:root:End of Epoch 6
INFO:root:Training loss: 2.798
INFO:root:Validation accuracy: 0.273, Validation loss: 3.10354
INFO:root:Best validation accuracy: 0.273 at epoch 6
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.00649
INFO:root:Validation iteration 8, Loss: 3.31439
INFO:root:Validation iteration 16, Loss: 3.26722
INFO:root:Validation iteration 24, Loss: 3.18751
INFO:root:Validation iteration 32, Loss: 3.01420
INFO:root:Validation iteration 40, Loss: 3.18987
INFO:root:Validation iteration 48, Loss: 3.13002
INFO:root:Validation iteration 56, Loss: 2.87046
INFO:root:Validation iteration 64, Loss: 2.85214
INFO:root:Validation iteration 72, Loss: 3.07811
INFO:root:Validation iteration 80, Loss: 2.81218
INFO:root:Validation iteration 88, Loss: 3.13624
INFO:root:Validation iteration 96, Loss: 2.90138
INFO:root:Validation iteration 104, Loss: 3.15031
INFO:root:Validation iteration 112, Loss: 3.19367
INFO:root:Validation iteration 120, Loss: 3.19192
INFO:root:Validation iteration 128, Loss: 3.12260
Test accuracy: 0.274, Test loss: 3.08768
INFO:root:Saving results...
INFO:root:Done!
"""

string20 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', test_root='./data/kaggle_testset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.', trained_model_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/temp/best_model_6.pth', predictions_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/predictions.csv'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size_model=32, batch_size_stats=128, train_split_size=0.75), 'train': TrainConfig(num_epochs=6, train_log_frequency=20, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='weighted_cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False, save_predictions=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/100
INFO:root:Processing batch 2/100
INFO:root:Processing batch 3/100
INFO:root:Processing batch 4/100
INFO:root:Processing batch 5/100
INFO:root:Processing batch 6/100
INFO:root:Processing batch 7/100
INFO:root:Processing batch 8/100
INFO:root:Processing batch 9/100
INFO:root:Processing batch 10/100
INFO:root:Processing batch 11/100
INFO:root:Processing batch 12/100
INFO:root:Processing batch 13/100
INFO:root:Processing batch 14/100
INFO:root:Processing batch 15/100
INFO:root:Processing batch 16/100
INFO:root:Processing batch 17/100
INFO:root:Processing batch 18/100
INFO:root:Processing batch 19/100
INFO:root:Processing batch 20/100
INFO:root:Processing batch 21/100
INFO:root:Processing batch 22/100
INFO:root:Processing batch 23/100
INFO:root:Processing batch 24/100
INFO:root:Processing batch 25/100
INFO:root:Processing batch 26/100
INFO:root:Processing batch 27/100
INFO:root:Processing batch 28/100
INFO:root:Processing batch 29/100
INFO:root:Processing batch 30/100
INFO:root:Processing batch 31/100
INFO:root:Processing batch 32/100
INFO:root:Processing batch 33/100
INFO:root:Processing batch 34/100
INFO:root:Processing batch 35/100
INFO:root:Processing batch 36/100
INFO:root:Processing batch 37/100
INFO:root:Processing batch 38/100
INFO:root:Processing batch 39/100
INFO:root:Processing batch 40/100
INFO:root:Processing batch 41/100
INFO:root:Processing batch 42/100
INFO:root:Processing batch 43/100
INFO:root:Processing batch 44/100
INFO:root:Processing batch 45/100
INFO:root:Processing batch 46/100
INFO:root:Processing batch 47/100
INFO:root:Processing batch 48/100
INFO:root:Processing batch 49/100
INFO:root:Processing batch 50/100
INFO:root:Processing batch 51/100
INFO:root:Processing batch 52/100
INFO:root:Processing batch 53/100
INFO:root:Processing batch 54/100
INFO:root:Processing batch 55/100
INFO:root:Processing batch 56/100
INFO:root:Processing batch 57/100
INFO:root:Processing batch 58/100
INFO:root:Processing batch 59/100
INFO:root:Processing batch 60/100
INFO:root:Processing batch 61/100
INFO:root:Processing batch 62/100
INFO:root:Processing batch 63/100
INFO:root:Processing batch 64/100
INFO:root:Processing batch 65/100
INFO:root:Processing batch 66/100
INFO:root:Processing batch 67/100
INFO:root:Processing batch 68/100
INFO:root:Processing batch 69/100
INFO:root:Processing batch 70/100
INFO:root:Processing batch 71/100
INFO:root:Processing batch 72/100
INFO:root:Processing batch 73/100
INFO:root:Processing batch 74/100
INFO:root:Processing batch 75/100
INFO:root:Processing batch 76/100
INFO:root:Processing batch 77/100
INFO:root:Processing batch 78/100
INFO:root:Processing batch 79/100
INFO:root:Processing batch 80/100
INFO:root:Processing batch 81/100
INFO:root:Processing batch 82/100
INFO:root:Processing batch 83/100
INFO:root:Processing batch 84/100
INFO:root:Processing batch 85/100
INFO:root:Processing batch 86/100
INFO:root:Processing batch 87/100
INFO:root:Processing batch 88/100
INFO:root:Processing batch 89/100
INFO:root:Processing batch 90/100
INFO:root:Processing batch 91/100
INFO:root:Processing batch 92/100
INFO:root:Processing batch 93/100
INFO:root:Processing batch 94/100
INFO:root:Processing batch 95/100
INFO:root:Processing batch 96/100
INFO:root:Processing batch 97/100
INFO:root:Processing batch 98/100
INFO:root:Processing batch 99/100
INFO:root:Processing batch 100/100
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47481051087379456, 0.4196726083755493, 0.3590790629386902], 'std': [0.27919673919677734, 0.27405110001564026, 0.2634223699569702], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47481051087379456, 0.4196726083755493, 0.3590790629386902], std=[0.27919673919677734, 0.27405110001564026, 0.2634223699569702])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.13975
INFO:root:Training epoch 1, Iteration 20, Loss: 4.97011
INFO:root:Training epoch 1, Iteration 40, Loss: 4.89981
INFO:root:Training epoch 1, Iteration 60, Loss: 4.72492
INFO:root:Training epoch 1, Iteration 80, Loss: 4.63505
INFO:root:Training epoch 1, Iteration 100, Loss: 4.51112
INFO:root:Training epoch 1, Iteration 120, Loss: 4.44929
INFO:root:Training epoch 1, Iteration 140, Loss: 4.42613
INFO:root:Training epoch 1, Iteration 160, Loss: 4.37708
INFO:root:Training epoch 1, Iteration 180, Loss: 4.32983
INFO:root:Training epoch 1, Iteration 200, Loss: 4.29290
INFO:root:Training epoch 1, Iteration 220, Loss: 4.30084
INFO:root:Training epoch 1, Iteration 240, Loss: 4.27907
INFO:root:Training epoch 1, Iteration 260, Loss: 4.24401
INFO:root:Training epoch 1, Iteration 280, Loss: 4.15787
INFO:root:Training epoch 1, Iteration 300, Loss: 4.28228
INFO:root:Training epoch 1, Iteration 320, Loss: 4.36268
INFO:root:Training epoch 1, Iteration 340, Loss: 4.16063
INFO:root:Training epoch 1, Iteration 360, Loss: 4.08313
INFO:root:Training epoch 1, Iteration 380, Loss: 4.22137
INFO:root:Validation iteration 1, Loss: 4.72598
INFO:root:Validation iteration 8, Loss: 4.39056
INFO:root:Validation iteration 16, Loss: 4.31514
INFO:root:Validation iteration 24, Loss: 4.43551
INFO:root:Validation iteration 32, Loss: 4.30768
INFO:root:Validation iteration 40, Loss: 4.14364
INFO:root:Validation iteration 48, Loss: 4.31544
INFO:root:Validation iteration 56, Loss: 4.19674
INFO:root:Validation iteration 64, Loss: 4.17648
INFO:root:Validation iteration 72, Loss: 4.51176
INFO:root:Validation iteration 80, Loss: 4.32679
INFO:root:Validation iteration 88, Loss: 4.48880
INFO:root:Validation iteration 96, Loss: 4.13460
INFO:root:Validation iteration 104, Loss: 4.18397
INFO:root:Validation iteration 112, Loss: 4.32860
INFO:root:Validation iteration 120, Loss: 4.28624
INFO:root:Validation iteration 128, Loss: 4.14791
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.392
INFO:root:Validation accuracy: 0.061, Validation loss: 4.29467
INFO:root:Training epoch 2, Iteration 1, Loss: 4.19870
INFO:root:Training epoch 2, Iteration 20, Loss: 4.10143
INFO:root:Training epoch 2, Iteration 40, Loss: 3.97773
INFO:root:Training epoch 2, Iteration 60, Loss: 4.08863
INFO:root:Training epoch 2, Iteration 80, Loss: 4.02961
INFO:root:Training epoch 2, Iteration 100, Loss: 3.99144
INFO:root:Training epoch 2, Iteration 120, Loss: 3.95684
INFO:root:Training epoch 2, Iteration 140, Loss: 3.97143
INFO:root:Training epoch 2, Iteration 160, Loss: 3.88538
INFO:root:Training epoch 2, Iteration 180, Loss: 3.97296
INFO:root:Training epoch 2, Iteration 200, Loss: 3.99081
INFO:root:Training epoch 2, Iteration 220, Loss: 3.97469
INFO:root:Training epoch 2, Iteration 240, Loss: 3.87107
INFO:root:Training epoch 2, Iteration 260, Loss: 3.90563
INFO:root:Training epoch 2, Iteration 280, Loss: 3.87280
INFO:root:Training epoch 2, Iteration 300, Loss: 3.83654
INFO:root:Training epoch 2, Iteration 320, Loss: 3.82760
INFO:root:Training epoch 2, Iteration 340, Loss: 3.92283
INFO:root:Training epoch 2, Iteration 360, Loss: 3.88813
INFO:root:Training epoch 2, Iteration 380, Loss: 3.82822
INFO:root:Validation iteration 1, Loss: 4.52049
INFO:root:Validation iteration 8, Loss: 3.96567
INFO:root:Validation iteration 16, Loss: 3.87468
INFO:root:Validation iteration 24, Loss: 3.87975
INFO:root:Validation iteration 32, Loss: 3.67338
INFO:root:Validation iteration 40, Loss: 3.70036
INFO:root:Validation iteration 48, Loss: 3.85467
INFO:root:Validation iteration 56, Loss: 3.77673
INFO:root:Validation iteration 64, Loss: 3.83159
INFO:root:Validation iteration 72, Loss: 3.76545
INFO:root:Validation iteration 80, Loss: 3.83931
INFO:root:Validation iteration 88, Loss: 3.98119
INFO:root:Validation iteration 96, Loss: 3.66692
INFO:root:Validation iteration 104, Loss: 3.61751
INFO:root:Validation iteration 112, Loss: 3.91369
INFO:root:Validation iteration 120, Loss: 3.80223
INFO:root:Validation iteration 128, Loss: 3.70180
INFO:root:End of Epoch 2
INFO:root:Training loss: 3.937
INFO:root:Validation accuracy: 0.108, Validation loss: 3.80504
INFO:root:Training epoch 3, Iteration 1, Loss: 3.20896
INFO:root:Training epoch 3, Iteration 20, Loss: 3.76903
INFO:root:Training epoch 3, Iteration 40, Loss: 3.76948
INFO:root:Training epoch 3, Iteration 60, Loss: 3.75132
INFO:root:Training epoch 3, Iteration 80, Loss: 3.67283
INFO:root:Training epoch 3, Iteration 100, Loss: 3.80390
INFO:root:Training epoch 3, Iteration 120, Loss: 3.63858
INFO:root:Training epoch 3, Iteration 140, Loss: 3.69504
INFO:root:Training epoch 3, Iteration 160, Loss: 3.83623
INFO:root:Training epoch 3, Iteration 180, Loss: 3.66129
INFO:root:Training epoch 3, Iteration 200, Loss: 3.54037
INFO:root:Training epoch 3, Iteration 220, Loss: 3.68377
INFO:root:Training epoch 3, Iteration 240, Loss: 3.60349
INFO:root:Training epoch 3, Iteration 260, Loss: 3.61755
INFO:root:Training epoch 3, Iteration 280, Loss: 3.61830
INFO:root:Training epoch 3, Iteration 300, Loss: 3.58771
INFO:root:Training epoch 3, Iteration 320, Loss: 3.71084
INFO:root:Training epoch 3, Iteration 340, Loss: 3.74664
INFO:root:Training epoch 3, Iteration 360, Loss: 3.76380
INFO:root:Training epoch 3, Iteration 380, Loss: 3.65317
INFO:root:Validation iteration 1, Loss: 4.20812
INFO:root:Validation iteration 8, Loss: 3.84855
INFO:root:Validation iteration 16, Loss: 3.64029
INFO:root:Validation iteration 24, Loss: 3.61378
INFO:root:Validation iteration 32, Loss: 3.62545
INFO:root:Validation iteration 40, Loss: 3.66029
INFO:root:Validation iteration 48, Loss: 3.65508
INFO:root:Validation iteration 56, Loss: 3.75594
INFO:root:Validation iteration 64, Loss: 3.69420
INFO:root:Validation iteration 72, Loss: 3.74452
INFO:root:Validation iteration 80, Loss: 3.73836
INFO:root:Validation iteration 88, Loss: 3.90156
INFO:root:Validation iteration 96, Loss: 3.47569
INFO:root:Validation iteration 104, Loss: 3.43575
INFO:root:Validation iteration 112, Loss: 3.75416
INFO:root:Validation iteration 120, Loss: 3.64681
INFO:root:Validation iteration 128, Loss: 3.61311
INFO:root:End of Epoch 3
INFO:root:Training loss: 3.685
INFO:root:Validation accuracy: 0.128, Validation loss: 3.68079
INFO:root:Training epoch 4, Iteration 1, Loss: 3.06038
INFO:root:Training epoch 4, Iteration 20, Loss: 3.56921
INFO:root:Training epoch 4, Iteration 40, Loss: 3.39740
INFO:root:Training epoch 4, Iteration 60, Loss: 3.47634
INFO:root:Training epoch 4, Iteration 80, Loss: 3.36432
INFO:root:Training epoch 4, Iteration 100, Loss: 3.56978
INFO:root:Training epoch 4, Iteration 120, Loss: 3.51629
INFO:root:Training epoch 4, Iteration 140, Loss: 3.44499
INFO:root:Training epoch 4, Iteration 160, Loss: 3.45579
INFO:root:Training epoch 4, Iteration 180, Loss: 3.63299
INFO:root:Training epoch 4, Iteration 200, Loss: 3.54298
INFO:root:Training epoch 4, Iteration 220, Loss: 3.50407
INFO:root:Training epoch 4, Iteration 240, Loss: 3.66058
INFO:root:Training epoch 4, Iteration 260, Loss: 3.54324
INFO:root:Training epoch 4, Iteration 280, Loss: 3.53732
INFO:root:Training epoch 4, Iteration 300, Loss: 3.44221
INFO:root:Training epoch 4, Iteration 320, Loss: 3.50882
INFO:root:Training epoch 4, Iteration 340, Loss: 3.54094
INFO:root:Training epoch 4, Iteration 360, Loss: 3.49046
INFO:root:Training epoch 4, Iteration 380, Loss: 3.48919
INFO:root:Validation iteration 1, Loss: 3.92539
INFO:root:Validation iteration 8, Loss: 3.65136
INFO:root:Validation iteration 16, Loss: 3.53865
INFO:root:Validation iteration 24, Loss: 3.52253
INFO:root:Validation iteration 32, Loss: 3.37281
INFO:root:Validation iteration 40, Loss: 3.41716
INFO:root:Validation iteration 48, Loss: 3.48188
INFO:root:Validation iteration 56, Loss: 3.50832
INFO:root:Validation iteration 64, Loss: 3.52037
INFO:root:Validation iteration 72, Loss: 3.45363
INFO:root:Validation iteration 80, Loss: 3.56225
INFO:root:Validation iteration 88, Loss: 3.73290
INFO:root:Validation iteration 96, Loss: 3.32162
INFO:root:Validation iteration 104, Loss: 3.34965
INFO:root:Validation iteration 112, Loss: 3.56734
INFO:root:Validation iteration 120, Loss: 3.53483
INFO:root:Validation iteration 128, Loss: 3.32753
INFO:root:End of Epoch 4
INFO:root:Training loss: 3.508
INFO:root:Validation accuracy: 0.162, Validation loss: 3.49992
INFO:root:Training epoch 5, Iteration 1, Loss: 3.52503
INFO:root:Training epoch 5, Iteration 20, Loss: 3.31980
INFO:root:Training epoch 5, Iteration 40, Loss: 3.37081
INFO:root:Training epoch 5, Iteration 60, Loss: 3.36034
INFO:root:Training epoch 5, Iteration 80, Loss: 3.37694
INFO:root:Training epoch 5, Iteration 100, Loss: 3.40810
INFO:root:Training epoch 5, Iteration 120, Loss: 3.31508
INFO:root:Training epoch 5, Iteration 140, Loss: 3.35783
INFO:root:Training epoch 5, Iteration 160, Loss: 3.36299
INFO:root:Training epoch 5, Iteration 180, Loss: 3.36214
INFO:root:Training epoch 5, Iteration 200, Loss: 3.28218
INFO:root:Training epoch 5, Iteration 220, Loss: 3.30227
INFO:root:Training epoch 5, Iteration 240, Loss: 3.31530
INFO:root:Training epoch 5, Iteration 260, Loss: 3.32548
INFO:root:Training epoch 5, Iteration 280, Loss: 3.35188
INFO:root:Training epoch 5, Iteration 300, Loss: 3.27989
INFO:root:Training epoch 5, Iteration 320, Loss: 3.39448
INFO:root:Training epoch 5, Iteration 340, Loss: 3.24470
INFO:root:Training epoch 5, Iteration 360, Loss: 3.33087
INFO:root:Training epoch 5, Iteration 380, Loss: 3.42466
INFO:root:Validation iteration 1, Loss: 4.02258
INFO:root:Validation iteration 8, Loss: 3.65192
INFO:root:Validation iteration 16, Loss: 3.49534
INFO:root:Validation iteration 24, Loss: 3.40791
INFO:root:Validation iteration 32, Loss: 3.31584
INFO:root:Validation iteration 40, Loss: 3.44362
INFO:root:Validation iteration 48, Loss: 3.50616
INFO:root:Validation iteration 56, Loss: 3.57323
INFO:root:Validation iteration 64, Loss: 3.46523
INFO:root:Validation iteration 72, Loss: 3.50534
INFO:root:Validation iteration 80, Loss: 3.46990
INFO:root:Validation iteration 88, Loss: 3.54133
INFO:root:Validation iteration 96, Loss: 3.31023
INFO:root:Validation iteration 104, Loss: 3.19028
INFO:root:Validation iteration 112, Loss: 3.41629
INFO:root:Validation iteration 120, Loss: 3.44022
INFO:root:Validation iteration 128, Loss: 3.29053
INFO:root:End of Epoch 5
INFO:root:Training loss: 3.340
INFO:root:Validation accuracy: 0.173, Validation loss: 3.44206
INFO:root:Training epoch 6, Iteration 1, Loss: 3.53608
INFO:root:Training epoch 6, Iteration 20, Loss: 3.24129
INFO:root:Training epoch 6, Iteration 40, Loss: 3.14902
INFO:root:Training epoch 6, Iteration 60, Loss: 3.16614
INFO:root:Training epoch 6, Iteration 80, Loss: 3.15821
INFO:root:Training epoch 6, Iteration 100, Loss: 3.08146
INFO:root:Training epoch 6, Iteration 120, Loss: 3.18118
INFO:root:Training epoch 6, Iteration 140, Loss: 3.16240
INFO:root:Training epoch 6, Iteration 160, Loss: 3.14670
INFO:root:Training epoch 6, Iteration 180, Loss: 3.22858
INFO:root:Training epoch 6, Iteration 200, Loss: 3.31569
INFO:root:Training epoch 6, Iteration 220, Loss: 3.16467
INFO:root:Training epoch 6, Iteration 240, Loss: 3.17818
INFO:root:Training epoch 6, Iteration 260, Loss: 3.30806
INFO:root:Training epoch 6, Iteration 280, Loss: 3.22260
INFO:root:Training epoch 6, Iteration 300, Loss: 3.15046
INFO:root:Training epoch 6, Iteration 320, Loss: 3.25060
INFO:root:Training epoch 6, Iteration 340, Loss: 3.21783
INFO:root:Training epoch 6, Iteration 360, Loss: 3.10221
INFO:root:Training epoch 6, Iteration 380, Loss: 3.17047
INFO:root:Validation iteration 1, Loss: 3.63277
INFO:root:Validation iteration 8, Loss: 3.52468
INFO:root:Validation iteration 16, Loss: 3.34240
INFO:root:Validation iteration 24, Loss: 3.29867
INFO:root:Validation iteration 32, Loss: 3.19482
INFO:root:Validation iteration 40, Loss: 3.32466
INFO:root:Validation iteration 48, Loss: 3.43543
INFO:root:Validation iteration 56, Loss: 3.39928
INFO:root:Validation iteration 64, Loss: 3.43990
INFO:root:Validation iteration 72, Loss: 3.39214
INFO:root:Validation iteration 80, Loss: 3.34146
INFO:root:Validation iteration 88, Loss: 3.53846
INFO:root:Validation iteration 96, Loss: 3.05377
INFO:root:Validation iteration 104, Loss: 3.18869
INFO:root:Validation iteration 112, Loss: 3.23860
INFO:root:Validation iteration 120, Loss: 3.28894
INFO:root:Validation iteration 128, Loss: 3.23366
INFO:root:End of Epoch 6
INFO:root:Training loss: 3.194
INFO:root:Validation accuracy: 0.194, Validation loss: 3.33257
INFO:root:Best validation accuracy: 0.194 at epoch 6
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.52417
INFO:root:Validation iteration 8, Loss: 3.70179
INFO:root:Validation iteration 16, Loss: 3.46010
INFO:root:Validation iteration 24, Loss: 3.42634
INFO:root:Validation iteration 32, Loss: 3.21400
INFO:root:Validation iteration 40, Loss: 3.45356
INFO:root:Validation iteration 48, Loss: 3.25023
INFO:root:Validation iteration 56, Loss: 3.11664
INFO:root:Validation iteration 64, Loss: 3.03189
INFO:root:Validation iteration 72, Loss: 3.22926
INFO:root:Validation iteration 80, Loss: 2.97675
INFO:root:Validation iteration 88, Loss: 3.29759
INFO:root:Validation iteration 96, Loss: 3.09592
INFO:root:Validation iteration 104, Loss: 3.22539
INFO:root:Validation iteration 112, Loss: 3.32275
INFO:root:Validation iteration 120, Loss: 3.35846
INFO:root:Validation iteration 128, Loss: 3.34458
Test accuracy: 0.201, Test loss: 3.28534
INFO:root:Saving results...
INFO:root:Done!
"""

string21 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', test_root='./data/kaggle_testset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.', trained_model_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/temp/best_model_5.pth', predictions_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/predictions.csv'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size_model=32, batch_size_stats=128, train_split_size=0.75), 'train': TrainConfig(num_epochs=6, train_log_frequency=20, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=1e-05, momentum=0.9, weight_decay=1e-06, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False, save_predictions=False, resume_training=True), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/100
INFO:root:Processing batch 2/100
INFO:root:Processing batch 3/100
INFO:root:Processing batch 4/100
INFO:root:Processing batch 5/100
INFO:root:Processing batch 6/100
INFO:root:Processing batch 7/100
INFO:root:Processing batch 8/100
INFO:root:Processing batch 9/100
INFO:root:Processing batch 10/100
INFO:root:Processing batch 11/100
INFO:root:Processing batch 12/100
INFO:root:Processing batch 13/100
INFO:root:Processing batch 14/100
INFO:root:Processing batch 15/100
INFO:root:Processing batch 16/100
INFO:root:Processing batch 17/100
INFO:root:Processing batch 18/100
INFO:root:Processing batch 19/100
INFO:root:Processing batch 20/100
INFO:root:Processing batch 21/100
INFO:root:Processing batch 22/100
INFO:root:Processing batch 23/100
INFO:root:Processing batch 24/100
INFO:root:Processing batch 25/100
INFO:root:Processing batch 26/100
INFO:root:Processing batch 27/100
INFO:root:Processing batch 28/100
INFO:root:Processing batch 29/100
INFO:root:Processing batch 30/100
INFO:root:Processing batch 31/100
INFO:root:Processing batch 32/100
INFO:root:Processing batch 33/100
INFO:root:Processing batch 34/100
INFO:root:Processing batch 35/100
INFO:root:Processing batch 36/100
INFO:root:Processing batch 37/100
INFO:root:Processing batch 38/100
INFO:root:Processing batch 39/100
INFO:root:Processing batch 40/100
INFO:root:Processing batch 41/100
INFO:root:Processing batch 42/100
INFO:root:Processing batch 43/100
INFO:root:Processing batch 44/100
INFO:root:Processing batch 45/100
INFO:root:Processing batch 46/100
INFO:root:Processing batch 47/100
INFO:root:Processing batch 48/100
INFO:root:Processing batch 49/100
INFO:root:Processing batch 50/100
INFO:root:Processing batch 51/100
INFO:root:Processing batch 52/100
INFO:root:Processing batch 53/100
INFO:root:Processing batch 54/100
INFO:root:Processing batch 55/100
INFO:root:Processing batch 56/100
INFO:root:Processing batch 57/100
INFO:root:Processing batch 58/100
INFO:root:Processing batch 59/100
INFO:root:Processing batch 60/100
INFO:root:Processing batch 61/100
INFO:root:Processing batch 62/100
INFO:root:Processing batch 63/100
INFO:root:Processing batch 64/100
INFO:root:Processing batch 65/100
INFO:root:Processing batch 66/100
INFO:root:Processing batch 67/100
INFO:root:Processing batch 68/100
INFO:root:Processing batch 69/100
INFO:root:Processing batch 70/100
INFO:root:Processing batch 71/100
INFO:root:Processing batch 72/100
INFO:root:Processing batch 73/100
INFO:root:Processing batch 74/100
INFO:root:Processing batch 75/100
INFO:root:Processing batch 76/100
INFO:root:Processing batch 77/100
INFO:root:Processing batch 78/100
INFO:root:Processing batch 79/100
INFO:root:Processing batch 80/100
INFO:root:Processing batch 81/100
INFO:root:Processing batch 82/100
INFO:root:Processing batch 83/100
INFO:root:Processing batch 84/100
INFO:root:Processing batch 85/100
INFO:root:Processing batch 86/100
INFO:root:Processing batch 87/100
INFO:root:Processing batch 88/100
INFO:root:Processing batch 89/100
INFO:root:Processing batch 90/100
INFO:root:Processing batch 91/100
INFO:root:Processing batch 92/100
INFO:root:Processing batch 93/100
INFO:root:Processing batch 94/100
INFO:root:Processing batch 95/100
INFO:root:Processing batch 96/100
INFO:root:Processing batch 97/100
INFO:root:Processing batch 98/100
INFO:root:Processing batch 99/100
INFO:root:Processing batch 100/100
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47481051087379456, 0.4196726083755493, 0.3590790629386902], 'std': [0.27919673919677734, 0.27405110001564026, 0.2634223699569702], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47481051087379456, 0.4196726083755493, 0.3590790629386902], std=[0.27919673919677734, 0.27405110001564026, 0.2634223699569702])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 3.50093
INFO:root:Training epoch 1, Iteration 20, Loss: 3.18304
INFO:root:Training epoch 1, Iteration 40, Loss: 2.98998
INFO:root:Training epoch 1, Iteration 60, Loss: 3.16731
INFO:root:Training epoch 1, Iteration 80, Loss: 3.08379
INFO:root:Training epoch 1, Iteration 100, Loss: 3.16147
INFO:root:Training epoch 1, Iteration 120, Loss: 2.95688
INFO:root:Training epoch 1, Iteration 140, Loss: 3.28879
INFO:root:Training epoch 1, Iteration 160, Loss: 3.00338
INFO:root:Training epoch 1, Iteration 180, Loss: 3.05357
INFO:root:Training epoch 1, Iteration 200, Loss: 3.09506
INFO:root:Training epoch 1, Iteration 220, Loss: 3.03182
INFO:root:Training epoch 1, Iteration 240, Loss: 3.08240
INFO:root:Training epoch 1, Iteration 260, Loss: 3.05930
INFO:root:Training epoch 1, Iteration 280, Loss: 3.05272
INFO:root:Training epoch 1, Iteration 300, Loss: 2.88079
INFO:root:Training epoch 1, Iteration 320, Loss: 3.01921
INFO:root:Training epoch 1, Iteration 340, Loss: 3.03148
INFO:root:Training epoch 1, Iteration 360, Loss: 3.04696
INFO:root:Training epoch 1, Iteration 380, Loss: 2.91248
INFO:root:Validation iteration 1, Loss: 3.56912
INFO:root:Validation iteration 8, Loss: 3.39112
INFO:root:Validation iteration 16, Loss: 3.12526
INFO:root:Validation iteration 24, Loss: 3.29027
INFO:root:Validation iteration 32, Loss: 3.08920
INFO:root:Validation iteration 40, Loss: 3.26569
INFO:root:Validation iteration 48, Loss: 3.25986
INFO:root:Validation iteration 56, Loss: 3.26392
INFO:root:Validation iteration 64, Loss: 3.10383
INFO:root:Validation iteration 72, Loss: 3.38937
INFO:root:Validation iteration 80, Loss: 3.17580
INFO:root:Validation iteration 88, Loss: 3.24312
INFO:root:Validation iteration 96, Loss: 3.13991
INFO:root:Validation iteration 104, Loss: 3.10742
INFO:root:Validation iteration 112, Loss: 3.36343
INFO:root:Validation iteration 120, Loss: 3.24960
INFO:root:Validation iteration 128, Loss: 3.22108
INFO:root:End of Epoch 1
INFO:root:Training loss: 3.055
INFO:root:Validation accuracy: 0.240, Validation loss: 3.23805
INFO:root:Training epoch 2, Iteration 1, Loss: 2.76210
INFO:root:Training epoch 2, Iteration 20, Loss: 3.00407
INFO:root:Training epoch 2, Iteration 40, Loss: 3.02398
INFO:root:Training epoch 2, Iteration 60, Loss: 2.97044
INFO:root:Training epoch 2, Iteration 80, Loss: 2.94090
INFO:root:Training epoch 2, Iteration 100, Loss: 3.03184
INFO:root:Training epoch 2, Iteration 120, Loss: 2.99553
INFO:root:Training epoch 2, Iteration 140, Loss: 2.96196
INFO:root:Training epoch 2, Iteration 160, Loss: 2.94649
INFO:root:Training epoch 2, Iteration 180, Loss: 2.89405
INFO:root:Training epoch 2, Iteration 200, Loss: 3.02248
INFO:root:Training epoch 2, Iteration 220, Loss: 2.87278
INFO:root:Training epoch 2, Iteration 240, Loss: 2.97864
INFO:root:Training epoch 2, Iteration 260, Loss: 2.88478
INFO:root:Training epoch 2, Iteration 280, Loss: 2.88400
INFO:root:Training epoch 2, Iteration 300, Loss: 3.02379
INFO:root:Training epoch 2, Iteration 320, Loss: 2.87532
INFO:root:Training epoch 2, Iteration 340, Loss: 3.01894
INFO:root:Training epoch 2, Iteration 360, Loss: 3.03053
INFO:root:Training epoch 2, Iteration 380, Loss: 2.89460
INFO:root:Validation iteration 1, Loss: 3.52198
INFO:root:Validation iteration 8, Loss: 3.37060
INFO:root:Validation iteration 16, Loss: 3.06214
INFO:root:Validation iteration 24, Loss: 3.19614
INFO:root:Validation iteration 32, Loss: 3.12793
INFO:root:Validation iteration 40, Loss: 3.28009
INFO:root:Validation iteration 48, Loss: 3.20879
INFO:root:Validation iteration 56, Loss: 3.25033
INFO:root:Validation iteration 64, Loss: 3.08450
INFO:root:Validation iteration 72, Loss: 3.31973
INFO:root:Validation iteration 80, Loss: 3.15388
INFO:root:Validation iteration 88, Loss: 3.21166
INFO:root:Validation iteration 96, Loss: 3.11830
INFO:root:Validation iteration 104, Loss: 3.03141
INFO:root:Validation iteration 112, Loss: 3.31146
INFO:root:Validation iteration 120, Loss: 3.19318
INFO:root:Validation iteration 128, Loss: 3.18888
INFO:root:End of Epoch 2
INFO:root:Training loss: 2.961
INFO:root:Validation accuracy: 0.243, Validation loss: 3.20150
INFO:root:Training epoch 3, Iteration 1, Loss: 2.24309
INFO:root:Training epoch 3, Iteration 20, Loss: 2.86613
INFO:root:Training epoch 3, Iteration 40, Loss: 3.02666
INFO:root:Training epoch 3, Iteration 60, Loss: 2.85510
INFO:root:Training epoch 3, Iteration 80, Loss: 2.87613
INFO:root:Training epoch 3, Iteration 100, Loss: 2.94179
INFO:root:Training epoch 3, Iteration 120, Loss: 2.81617
INFO:root:Training epoch 3, Iteration 140, Loss: 2.84044
INFO:root:Training epoch 3, Iteration 160, Loss: 2.96340
INFO:root:Training epoch 3, Iteration 180, Loss: 2.83625
INFO:root:Training epoch 3, Iteration 200, Loss: 3.00667
INFO:root:Training epoch 3, Iteration 220, Loss: 3.00672
INFO:root:Training epoch 3, Iteration 240, Loss: 2.94558
INFO:root:Training epoch 3, Iteration 260, Loss: 2.88173
INFO:root:Training epoch 3, Iteration 280, Loss: 2.74254
INFO:root:Training epoch 3, Iteration 300, Loss: 2.87323
INFO:root:Training epoch 3, Iteration 320, Loss: 2.98155
INFO:root:Training epoch 3, Iteration 340, Loss: 2.87347
INFO:root:Training epoch 3, Iteration 360, Loss: 2.94271
INFO:root:Training epoch 3, Iteration 380, Loss: 2.99994
INFO:root:Validation iteration 1, Loss: 3.52982
INFO:root:Validation iteration 8, Loss: 3.36503
INFO:root:Validation iteration 16, Loss: 3.06092
INFO:root:Validation iteration 24, Loss: 3.17286
INFO:root:Validation iteration 32, Loss: 3.14273
INFO:root:Validation iteration 40, Loss: 3.25294
INFO:root:Validation iteration 48, Loss: 3.19353
INFO:root:Validation iteration 56, Loss: 3.20556
INFO:root:Validation iteration 64, Loss: 3.05922
INFO:root:Validation iteration 72, Loss: 3.32529
INFO:root:Validation iteration 80, Loss: 3.12356
INFO:root:Validation iteration 88, Loss: 3.17289
INFO:root:Validation iteration 96, Loss: 3.06702
INFO:root:Validation iteration 104, Loss: 2.96681
INFO:root:Validation iteration 112, Loss: 3.26414
INFO:root:Validation iteration 120, Loss: 3.12282
INFO:root:Validation iteration 128, Loss: 3.14591
INFO:root:End of Epoch 3
INFO:root:Training loss: 2.911
INFO:root:Validation accuracy: 0.251, Validation loss: 3.17285
INFO:root:Training epoch 4, Iteration 1, Loss: 3.00449
INFO:root:Training epoch 4, Iteration 20, Loss: 2.88507
INFO:root:Training epoch 4, Iteration 40, Loss: 2.85058
INFO:root:Training epoch 4, Iteration 60, Loss: 2.86729
INFO:root:Training epoch 4, Iteration 80, Loss: 2.77732
INFO:root:Training epoch 4, Iteration 100, Loss: 2.86549
INFO:root:Training epoch 4, Iteration 120, Loss: 2.83437
INFO:root:Training epoch 4, Iteration 140, Loss: 2.79532
INFO:root:Training epoch 4, Iteration 160, Loss: 2.81497
INFO:root:Training epoch 4, Iteration 180, Loss: 2.80415
INFO:root:Training epoch 4, Iteration 200, Loss: 3.05841
INFO:root:Training epoch 4, Iteration 220, Loss: 2.96911
INFO:root:Training epoch 4, Iteration 240, Loss: 2.87118
INFO:root:Training epoch 4, Iteration 260, Loss: 2.75033
INFO:root:Training epoch 4, Iteration 280, Loss: 2.91824
INFO:root:Training epoch 4, Iteration 300, Loss: 2.88985
INFO:root:Training epoch 4, Iteration 320, Loss: 2.97057
INFO:root:Training epoch 4, Iteration 340, Loss: 2.91758
INFO:root:Training epoch 4, Iteration 360, Loss: 2.89459
INFO:root:Training epoch 4, Iteration 380, Loss: 2.82746
INFO:root:Validation iteration 1, Loss: 3.53178
INFO:root:Validation iteration 8, Loss: 3.34741
INFO:root:Validation iteration 16, Loss: 3.03837
INFO:root:Validation iteration 24, Loss: 3.13444
INFO:root:Validation iteration 32, Loss: 3.06217
INFO:root:Validation iteration 40, Loss: 3.20520
INFO:root:Validation iteration 48, Loss: 3.19210
INFO:root:Validation iteration 56, Loss: 3.14683
INFO:root:Validation iteration 64, Loss: 3.07277
INFO:root:Validation iteration 72, Loss: 3.29252
INFO:root:Validation iteration 80, Loss: 3.08735
INFO:root:Validation iteration 88, Loss: 3.14468
INFO:root:Validation iteration 96, Loss: 3.09694
INFO:root:Validation iteration 104, Loss: 2.99783
INFO:root:Validation iteration 112, Loss: 3.21079
INFO:root:Validation iteration 120, Loss: 3.12165
INFO:root:Validation iteration 128, Loss: 3.10402
INFO:root:End of Epoch 4
INFO:root:Training loss: 2.874
INFO:root:Validation accuracy: 0.255, Validation loss: 3.14879
INFO:root:Training epoch 5, Iteration 1, Loss: 2.44512
INFO:root:Training epoch 5, Iteration 20, Loss: 2.85043
INFO:root:Training epoch 5, Iteration 40, Loss: 2.86542
INFO:root:Training epoch 5, Iteration 60, Loss: 2.91231
INFO:root:Training epoch 5, Iteration 80, Loss: 2.86013
INFO:root:Training epoch 5, Iteration 100, Loss: 2.87456
INFO:root:Training epoch 5, Iteration 120, Loss: 2.74984
INFO:root:Training epoch 5, Iteration 140, Loss: 2.80686
INFO:root:Training epoch 5, Iteration 160, Loss: 2.88553
INFO:root:Training epoch 5, Iteration 180, Loss: 2.81675
INFO:root:Training epoch 5, Iteration 200, Loss: 2.93325
INFO:root:Training epoch 5, Iteration 220, Loss: 2.83990
INFO:root:Training epoch 5, Iteration 240, Loss: 2.92768
INFO:root:Training epoch 5, Iteration 260, Loss: 2.90840
INFO:root:Training epoch 5, Iteration 280, Loss: 2.84588
INFO:root:Training epoch 5, Iteration 300, Loss: 2.76744
INFO:root:Training epoch 5, Iteration 320, Loss: 2.93801
INFO:root:Training epoch 5, Iteration 340, Loss: 2.72428
INFO:root:Training epoch 5, Iteration 360, Loss: 2.78392
INFO:root:Training epoch 5, Iteration 380, Loss: 2.71816
INFO:root:Validation iteration 1, Loss: 3.50120
INFO:root:Validation iteration 8, Loss: 3.28367
INFO:root:Validation iteration 16, Loss: 3.01305
INFO:root:Validation iteration 24, Loss: 3.13452
INFO:root:Validation iteration 32, Loss: 3.01898
INFO:root:Validation iteration 40, Loss: 3.17825
INFO:root:Validation iteration 48, Loss: 3.16577
INFO:root:Validation iteration 56, Loss: 3.14397
INFO:root:Validation iteration 64, Loss: 3.05317
INFO:root:Validation iteration 72, Loss: 3.22827
INFO:root:Validation iteration 80, Loss: 3.08537
INFO:root:Validation iteration 88, Loss: 3.09135
INFO:root:Validation iteration 96, Loss: 3.03008
INFO:root:Validation iteration 104, Loss: 2.94980
INFO:root:Validation iteration 112, Loss: 3.20556
INFO:root:Validation iteration 120, Loss: 3.12891
INFO:root:Validation iteration 128, Loss: 3.14711
INFO:root:End of Epoch 5
INFO:root:Training loss: 2.844
INFO:root:Validation accuracy: 0.257, Validation loss: 3.12519
INFO:root:Training epoch 6, Iteration 1, Loss: 2.91372
INFO:root:Training epoch 6, Iteration 20, Loss: 2.80052
INFO:root:Training epoch 6, Iteration 40, Loss: 2.70365
INFO:root:Training epoch 6, Iteration 60, Loss: 2.88201
INFO:root:Training epoch 6, Iteration 80, Loss: 2.87299
INFO:root:Training epoch 6, Iteration 100, Loss: 2.77189
INFO:root:Training epoch 6, Iteration 120, Loss: 2.70526
INFO:root:Training epoch 6, Iteration 140, Loss: 2.71294
INFO:root:Training epoch 6, Iteration 160, Loss: 2.85033
INFO:root:Training epoch 6, Iteration 180, Loss: 2.69368
INFO:root:Training epoch 6, Iteration 200, Loss: 2.78561
INFO:root:Training epoch 6, Iteration 220, Loss: 2.84962
INFO:root:Training epoch 6, Iteration 240, Loss: 2.83609
INFO:root:Training epoch 6, Iteration 260, Loss: 2.72996
INFO:root:Training epoch 6, Iteration 280, Loss: 2.82553
INFO:root:Training epoch 6, Iteration 300, Loss: 2.85564
INFO:root:Training epoch 6, Iteration 320, Loss: 2.75325
INFO:root:Training epoch 6, Iteration 340, Loss: 2.81630
INFO:root:Training epoch 6, Iteration 360, Loss: 2.75962
INFO:root:Training epoch 6, Iteration 380, Loss: 2.87026
INFO:root:Validation iteration 1, Loss: 3.48970
INFO:root:Validation iteration 8, Loss: 3.33815
INFO:root:Validation iteration 16, Loss: 2.99386
INFO:root:Validation iteration 24, Loss: 3.12000
INFO:root:Validation iteration 32, Loss: 3.01702
INFO:root:Validation iteration 40, Loss: 3.15947
INFO:root:Validation iteration 48, Loss: 3.16845
INFO:root:Validation iteration 56, Loss: 3.09039
INFO:root:Validation iteration 64, Loss: 2.98308
INFO:root:Validation iteration 72, Loss: 3.24325
INFO:root:Validation iteration 80, Loss: 3.06659
INFO:root:Validation iteration 88, Loss: 3.09855
INFO:root:Validation iteration 96, Loss: 3.01573
INFO:root:Validation iteration 104, Loss: 2.90705
INFO:root:Validation iteration 112, Loss: 3.20666
INFO:root:Validation iteration 120, Loss: 3.09887
INFO:root:Validation iteration 128, Loss: 3.01241
INFO:root:End of Epoch 6
INFO:root:Training loss: 2.798
INFO:root:Validation accuracy: 0.273, Validation loss: 3.10354
INFO:root:Best validation accuracy: 0.273 at epoch 6
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.00649
INFO:root:Validation iteration 8, Loss: 3.31439
INFO:root:Validation iteration 16, Loss: 3.26722
INFO:root:Validation iteration 24, Loss: 3.18751
INFO:root:Validation iteration 32, Loss: 3.01420
INFO:root:Validation iteration 40, Loss: 3.18987
INFO:root:Validation iteration 48, Loss: 3.13002
INFO:root:Validation iteration 56, Loss: 2.87046
INFO:root:Validation iteration 64, Loss: 2.85214
INFO:root:Validation iteration 72, Loss: 3.07811
INFO:root:Validation iteration 80, Loss: 2.81218
INFO:root:Validation iteration 88, Loss: 3.13624
INFO:root:Validation iteration 96, Loss: 2.90138
INFO:root:Validation iteration 104, Loss: 3.15031
INFO:root:Validation iteration 112, Loss: 3.19367
INFO:root:Validation iteration 120, Loss: 3.19192
INFO:root:Validation iteration 128, Loss: 3.12260
Test accuracy: 0.274, Test loss: 3.08768
INFO:root:Saving results...
INFO:root:Done!
"""

string21 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', test_root='./data/kaggle_testset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.', trained_model_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/temp/best_model_5.pth', predictions_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/predictions.csv'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size_model=16, batch_size_stats=128, train_split_size=0.75), 'train': TrainConfig(num_epochs=5, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False, save_predictions=False, resume_training=False), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/100
INFO:root:Processing batch 2/100
INFO:root:Processing batch 3/100
INFO:root:Processing batch 4/100
INFO:root:Processing batch 5/100
INFO:root:Processing batch 6/100
INFO:root:Processing batch 7/100
INFO:root:Processing batch 8/100
INFO:root:Processing batch 9/100
INFO:root:Processing batch 10/100
INFO:root:Processing batch 11/100
INFO:root:Processing batch 12/100
INFO:root:Processing batch 13/100
INFO:root:Processing batch 14/100
INFO:root:Processing batch 15/100
INFO:root:Processing batch 16/100
INFO:root:Processing batch 17/100
INFO:root:Processing batch 18/100
INFO:root:Processing batch 19/100
INFO:root:Processing batch 20/100
INFO:root:Processing batch 21/100
INFO:root:Processing batch 22/100
INFO:root:Processing batch 23/100
INFO:root:Processing batch 24/100
INFO:root:Processing batch 25/100
INFO:root:Processing batch 26/100
INFO:root:Processing batch 27/100
INFO:root:Processing batch 28/100
INFO:root:Processing batch 29/100
INFO:root:Processing batch 30/100
INFO:root:Processing batch 31/100
INFO:root:Processing batch 32/100
INFO:root:Processing batch 33/100
INFO:root:Processing batch 34/100
INFO:root:Processing batch 35/100
INFO:root:Processing batch 36/100
INFO:root:Processing batch 37/100
INFO:root:Processing batch 38/100
INFO:root:Processing batch 39/100
INFO:root:Processing batch 40/100
INFO:root:Processing batch 41/100
INFO:root:Processing batch 42/100
INFO:root:Processing batch 43/100
INFO:root:Processing batch 44/100
INFO:root:Processing batch 45/100
INFO:root:Processing batch 46/100
INFO:root:Processing batch 47/100
INFO:root:Processing batch 48/100
INFO:root:Processing batch 49/100
INFO:root:Processing batch 50/100
INFO:root:Processing batch 51/100
INFO:root:Processing batch 52/100
INFO:root:Processing batch 53/100
INFO:root:Processing batch 54/100
INFO:root:Processing batch 55/100
INFO:root:Processing batch 56/100
INFO:root:Processing batch 57/100
INFO:root:Processing batch 58/100
INFO:root:Processing batch 59/100
INFO:root:Processing batch 60/100
INFO:root:Processing batch 61/100
INFO:root:Processing batch 62/100
INFO:root:Processing batch 63/100
INFO:root:Processing batch 64/100
INFO:root:Processing batch 65/100
INFO:root:Processing batch 66/100
INFO:root:Processing batch 67/100
INFO:root:Processing batch 68/100
INFO:root:Processing batch 69/100
INFO:root:Processing batch 70/100
INFO:root:Processing batch 71/100
INFO:root:Processing batch 72/100
INFO:root:Processing batch 73/100
INFO:root:Processing batch 74/100
INFO:root:Processing batch 75/100
INFO:root:Processing batch 76/100
INFO:root:Processing batch 77/100
INFO:root:Processing batch 78/100
INFO:root:Processing batch 79/100
INFO:root:Processing batch 80/100
INFO:root:Processing batch 81/100
INFO:root:Processing batch 82/100
INFO:root:Processing batch 83/100
INFO:root:Processing batch 84/100
INFO:root:Processing batch 85/100
INFO:root:Processing batch 86/100
INFO:root:Processing batch 87/100
INFO:root:Processing batch 88/100
INFO:root:Processing batch 89/100
INFO:root:Processing batch 90/100
INFO:root:Processing batch 91/100
INFO:root:Processing batch 92/100
INFO:root:Processing batch 93/100
INFO:root:Processing batch 94/100
INFO:root:Processing batch 95/100
INFO:root:Processing batch 96/100
INFO:root:Processing batch 97/100
INFO:root:Processing batch 98/100
INFO:root:Processing batch 99/100
INFO:root:Processing batch 100/100
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47481051087379456, 0.4196726083755493, 0.3590790629386902], 'std': [0.27919673919677734, 0.27405110001564026, 0.2634223699569702], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47481051087379456, 0.4196726083755493, 0.3590790629386902], std=[0.27919673919677734, 0.27405110001564026, 0.2634223699569702])']}}}
Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to /root/.cache/torch/hub/checkpoints/resnet18-f37072fd.pth
100% 44.7M/44.7M [00:00<00:00, 163MB/s]
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.15178
INFO:root:Training epoch 1, Iteration 30, Loss: 5.02921
INFO:root:Training epoch 1, Iteration 60, Loss: 5.01457
INFO:root:Training epoch 1, Iteration 90, Loss: 4.79668
INFO:root:Training epoch 1, Iteration 120, Loss: 4.72159
INFO:root:Training epoch 1, Iteration 150, Loss: 4.69132
INFO:root:Training epoch 1, Iteration 180, Loss: 4.59120
INFO:root:Training epoch 1, Iteration 210, Loss: 4.62345
INFO:root:Training epoch 1, Iteration 240, Loss: 4.52154
INFO:root:Training epoch 1, Iteration 270, Loss: 4.64369
INFO:root:Training epoch 1, Iteration 300, Loss: 4.51903
INFO:root:Training epoch 1, Iteration 330, Loss: 4.49264
INFO:root:Training epoch 1, Iteration 360, Loss: 4.40600
INFO:root:Training epoch 1, Iteration 390, Loss: 4.51068
INFO:root:Training epoch 1, Iteration 420, Loss: 4.42263
INFO:root:Training epoch 1, Iteration 450, Loss: 4.37740
INFO:root:Training epoch 1, Iteration 480, Loss: 4.45289
INFO:root:Training epoch 1, Iteration 510, Loss: 4.46217
INFO:root:Training epoch 1, Iteration 540, Loss: 4.36801
INFO:root:Training epoch 1, Iteration 570, Loss: 4.31361
INFO:root:Training epoch 1, Iteration 600, Loss: 4.23779
INFO:root:Training epoch 1, Iteration 630, Loss: 4.29735
INFO:root:Training epoch 1, Iteration 660, Loss: 4.31588
INFO:root:Training epoch 1, Iteration 690, Loss: 4.42088
INFO:root:Training epoch 1, Iteration 720, Loss: 4.21942
INFO:root:Training epoch 1, Iteration 750, Loss: 4.26941
INFO:root:Training epoch 1, Iteration 780, Loss: 4.27275
INFO:root:Validation iteration 1, Loss: 4.57487
INFO:root:Validation iteration 10, Loss: 4.27199
INFO:root:Validation iteration 20, Loss: 4.09219
INFO:root:Validation iteration 30, Loss: 4.28775
INFO:root:Validation iteration 40, Loss: 4.25745
INFO:root:Validation iteration 50, Loss: 4.31360
INFO:root:Validation iteration 60, Loss: 4.31513
INFO:root:Validation iteration 70, Loss: 4.20135
INFO:root:Validation iteration 80, Loss: 4.07225
INFO:root:Validation iteration 90, Loss: 3.92641
INFO:root:Validation iteration 100, Loss: 4.26888
INFO:root:Validation iteration 110, Loss: 4.30890
INFO:root:Validation iteration 120, Loss: 3.99773
INFO:root:Validation iteration 130, Loss: 4.22564
INFO:root:Validation iteration 140, Loss: 4.25001
INFO:root:Validation iteration 150, Loss: 4.31181
INFO:root:Validation iteration 160, Loss: 4.30437
INFO:root:Validation iteration 170, Loss: 4.10736
INFO:root:Validation iteration 180, Loss: 4.27446
INFO:root:Validation iteration 190, Loss: 4.18503
INFO:root:Validation iteration 200, Loss: 3.99839
INFO:root:Validation iteration 210, Loss: 4.14526
INFO:root:Validation iteration 220, Loss: 4.20320
INFO:root:Validation iteration 230, Loss: 4.37102
INFO:root:Validation iteration 240, Loss: 4.32125
INFO:root:Validation iteration 250, Loss: 4.44535
INFO:root:Validation iteration 260, Loss: 4.18483
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.492
INFO:root:Validation accuracy: 0.074, Validation loss: 4.21978
INFO:root:Training epoch 2, Iteration 1, Loss: 3.83437
INFO:root:Training epoch 2, Iteration 30, Loss: 4.13168
INFO:root:Training epoch 2, Iteration 60, Loss: 4.20456
INFO:root:Training epoch 2, Iteration 90, Loss: 4.21763
INFO:root:Training epoch 2, Iteration 120, Loss: 4.16654
INFO:root:Training epoch 2, Iteration 150, Loss: 4.09829
INFO:root:Training epoch 2, Iteration 180, Loss: 4.14683
INFO:root:Training epoch 2, Iteration 210, Loss: 4.13705
INFO:root:Training epoch 2, Iteration 240, Loss: 4.03319
INFO:root:Training epoch 2, Iteration 270, Loss: 4.12959
INFO:root:Training epoch 2, Iteration 300, Loss: 4.10562
INFO:root:Training epoch 2, Iteration 330, Loss: 4.18190
INFO:root:Training epoch 2, Iteration 360, Loss: 4.06234
INFO:root:Training epoch 2, Iteration 390, Loss: 4.02085
INFO:root:Training epoch 2, Iteration 420, Loss: 4.09482
INFO:root:Training epoch 2, Iteration 450, Loss: 4.07704
INFO:root:Training epoch 2, Iteration 480, Loss: 3.99065
INFO:root:Training epoch 2, Iteration 510, Loss: 3.96792
INFO:root:Training epoch 2, Iteration 540, Loss: 4.04688
INFO:root:Training epoch 2, Iteration 570, Loss: 4.05061
INFO:root:Training epoch 2, Iteration 600, Loss: 4.06570
INFO:root:Training epoch 2, Iteration 630, Loss: 4.03188
INFO:root:Training epoch 2, Iteration 660, Loss: 4.13249
INFO:root:Training epoch 2, Iteration 690, Loss: 3.87348
INFO:root:Training epoch 2, Iteration 720, Loss: 4.09722
INFO:root:Training epoch 2, Iteration 750, Loss: 3.95975
INFO:root:Training epoch 2, Iteration 780, Loss: 4.01471
INFO:root:Validation iteration 1, Loss: 4.48404
INFO:root:Validation iteration 10, Loss: 4.40814
INFO:root:Validation iteration 20, Loss: 4.60011
INFO:root:Validation iteration 30, Loss: 5.16891
INFO:root:Validation iteration 40, Loss: 4.70818
INFO:root:Validation iteration 50, Loss: 4.40330
INFO:root:Validation iteration 60, Loss: 4.42304
INFO:root:Validation iteration 70, Loss: 5.03886
INFO:root:Validation iteration 80, Loss: 4.66357
INFO:root:Validation iteration 90, Loss: 4.14671
INFO:root:Validation iteration 100, Loss: 4.74049
INFO:root:Validation iteration 110, Loss: 5.29471
INFO:root:Validation iteration 120, Loss: 4.68674
INFO:root:Validation iteration 130, Loss: 4.71893
INFO:root:Validation iteration 140, Loss: 4.83059
INFO:root:Validation iteration 150, Loss: 5.03697
INFO:root:Validation iteration 160, Loss: 4.12131
INFO:root:Validation iteration 170, Loss: 5.24830
INFO:root:Validation iteration 180, Loss: 4.81833
INFO:root:Validation iteration 190, Loss: 4.70622
INFO:root:Validation iteration 200, Loss: 4.51143
INFO:root:Validation iteration 210, Loss: 4.53765
INFO:root:Validation iteration 220, Loss: 5.40977
INFO:root:Validation iteration 230, Loss: 4.89002
INFO:root:Validation iteration 240, Loss: 4.84912
INFO:root:Validation iteration 250, Loss: 4.62248
INFO:root:Validation iteration 260, Loss: 4.99014
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.079
INFO:root:Validation accuracy: 0.097, Validation loss: 4.73717
INFO:root:Training epoch 3, Iteration 1, Loss: 3.85116
INFO:root:Training epoch 3, Iteration 30, Loss: 3.87812
INFO:root:Training epoch 3, Iteration 60, Loss: 3.96953
INFO:root:Training epoch 3, Iteration 90, Loss: 3.88018
INFO:root:Training epoch 3, Iteration 120, Loss: 3.88083
INFO:root:Training epoch 3, Iteration 150, Loss: 3.89023
INFO:root:Training epoch 3, Iteration 180, Loss: 3.80124
INFO:root:Training epoch 3, Iteration 210, Loss: 3.95252
INFO:root:Training epoch 3, Iteration 240, Loss: 3.73656
INFO:root:Training epoch 3, Iteration 270, Loss: 3.85829
INFO:root:Training epoch 3, Iteration 300, Loss: 3.90267
INFO:root:Training epoch 3, Iteration 330, Loss: 3.80957
INFO:root:Training epoch 3, Iteration 360, Loss: 3.88938
INFO:root:Training epoch 3, Iteration 390, Loss: 3.83598
INFO:root:Training epoch 3, Iteration 420, Loss: 3.90698
INFO:root:Training epoch 3, Iteration 450, Loss: 3.70464
INFO:root:Training epoch 3, Iteration 480, Loss: 3.86562
INFO:root:Training epoch 3, Iteration 510, Loss: 3.76525
INFO:root:Training epoch 3, Iteration 540, Loss: 3.82602
INFO:root:Training epoch 3, Iteration 570, Loss: 3.76263
INFO:root:Training epoch 3, Iteration 600, Loss: 3.96315
INFO:root:Training epoch 3, Iteration 630, Loss: 3.88230
INFO:root:Training epoch 3, Iteration 660, Loss: 3.88120
INFO:root:Training epoch 3, Iteration 690, Loss: 3.79220
INFO:root:Training epoch 3, Iteration 720, Loss: 3.87938
INFO:root:Training epoch 3, Iteration 750, Loss: 3.87550
INFO:root:Training epoch 3, Iteration 780, Loss: 3.70774
INFO:root:Validation iteration 1, Loss: 4.00310
INFO:root:Validation iteration 10, Loss: 4.02681
INFO:root:Validation iteration 20, Loss: 3.95500
INFO:root:Validation iteration 30, Loss: 26.98535
INFO:root:Validation iteration 40, Loss: 3.80369
INFO:root:Validation iteration 50, Loss: 4.02548
INFO:root:Validation iteration 60, Loss: 32.66398
INFO:root:Validation iteration 70, Loss: 4.33477
INFO:root:Validation iteration 80, Loss: 4.21976
INFO:root:Validation iteration 90, Loss: 37.66865
INFO:root:Validation iteration 100, Loss: 37.70919
INFO:root:Validation iteration 110, Loss: 10.60024
INFO:root:Validation iteration 120, Loss: 24.86375
INFO:root:Validation iteration 130, Loss: 4.06167
INFO:root:Validation iteration 140, Loss: 4.20973
INFO:root:Validation iteration 150, Loss: 19.23849
INFO:root:Validation iteration 160, Loss: 7.44095
INFO:root:Validation iteration 170, Loss: 6.26289
INFO:root:Validation iteration 180, Loss: 48.79415
INFO:root:Validation iteration 190, Loss: 4.08909
INFO:root:Validation iteration 200, Loss: 46.48693
INFO:root:Validation iteration 210, Loss: 26.31797
INFO:root:Validation iteration 220, Loss: 6.35061
INFO:root:Validation iteration 230, Loss: 13.27390
INFO:root:Validation iteration 240, Loss: 5.81207
INFO:root:Validation iteration 250, Loss: 74.49734
INFO:root:Validation iteration 260, Loss: 15.17099
INFO:root:End of Epoch 3
INFO:root:Training loss: 3.847
INFO:root:Validation accuracy: 0.131, Validation loss: 19.74149
INFO:root:Training epoch 4, Iteration 1, Loss: 3.45945
INFO:root:Training epoch 4, Iteration 30, Loss: 3.65028
INFO:root:Training epoch 4, Iteration 60, Loss: 3.56524
INFO:root:Training epoch 4, Iteration 90, Loss: 3.62172
INFO:root:Training epoch 4, Iteration 120, Loss: 3.73656
INFO:root:Training epoch 4, Iteration 150, Loss: 3.73556
INFO:root:Training epoch 4, Iteration 180, Loss: 3.74330
INFO:root:Training epoch 4, Iteration 210, Loss: 3.70755
INFO:root:Training epoch 4, Iteration 240, Loss: 3.57032
INFO:root:Training epoch 4, Iteration 270, Loss: 3.62385
INFO:root:Training epoch 4, Iteration 300, Loss: 3.75790
INFO:root:Training epoch 4, Iteration 330, Loss: 3.66016
INFO:root:Training epoch 4, Iteration 360, Loss: 3.70440
INFO:root:Training epoch 4, Iteration 390, Loss: 3.66758
INFO:root:Training epoch 4, Iteration 420, Loss: 3.57106
INFO:root:Training epoch 4, Iteration 450, Loss: 3.60410
INFO:root:Training epoch 4, Iteration 480, Loss: 3.86575
INFO:root:Training epoch 4, Iteration 510, Loss: 3.59232
INFO:root:Training epoch 4, Iteration 540, Loss: 3.70144
INFO:root:Training epoch 4, Iteration 570, Loss: 3.58188
INFO:root:Training epoch 4, Iteration 600, Loss: 3.66456
INFO:root:Training epoch 4, Iteration 630, Loss: 3.75088
INFO:root:Training epoch 4, Iteration 660, Loss: 3.64261
INFO:root:Training epoch 4, Iteration 690, Loss: 3.60865
INFO:root:Training epoch 4, Iteration 720, Loss: 3.64189
INFO:root:Training epoch 4, Iteration 750, Loss: 3.58532
INFO:root:Training epoch 4, Iteration 780, Loss: 3.61955
INFO:root:Validation iteration 1, Loss: 4.21661
INFO:root:Validation iteration 10, Loss: 3.71517
INFO:root:Validation iteration 20, Loss: 3.94200
INFO:root:Validation iteration 30, Loss: 3.87904
INFO:root:Validation iteration 40, Loss: 3.93619
INFO:root:Validation iteration 50, Loss: 3.68399
INFO:root:Validation iteration 60, Loss: 4.32800
INFO:root:Validation iteration 70, Loss: 4.11355
INFO:root:Validation iteration 80, Loss: 4.17803
INFO:root:Validation iteration 90, Loss: 3.46002
INFO:root:Validation iteration 100, Loss: 3.61422
INFO:root:Validation iteration 110, Loss: 4.56227
INFO:root:Validation iteration 120, Loss: 3.54259
INFO:root:Validation iteration 130, Loss: 3.63028
INFO:root:Validation iteration 140, Loss: 3.86731
INFO:root:Validation iteration 150, Loss: 3.74310
INFO:root:Validation iteration 160, Loss: 3.63544
INFO:root:Validation iteration 170, Loss: 3.59291
INFO:root:Validation iteration 180, Loss: 3.77035
INFO:root:Validation iteration 190, Loss: 3.57643
INFO:root:Validation iteration 200, Loss: 3.71035
INFO:root:Validation iteration 210, Loss: 3.51070
INFO:root:Validation iteration 220, Loss: 3.75517
INFO:root:Validation iteration 230, Loss: 3.76898
INFO:root:Validation iteration 240, Loss: 4.29921
INFO:root:Validation iteration 250, Loss: 4.15667
INFO:root:Validation iteration 260, Loss: 3.58022
INFO:root:End of Epoch 4
INFO:root:Training loss: 3.656
INFO:root:Validation accuracy: 0.170, Validation loss: 3.82934
INFO:root:Training epoch 5, Iteration 1, Loss: 3.70175
INFO:root:Training epoch 5, Iteration 30, Loss: 3.63426
INFO:root:Training epoch 5, Iteration 60, Loss: 3.40560
INFO:root:Training epoch 5, Iteration 90, Loss: 3.45826
INFO:root:Training epoch 5, Iteration 120, Loss: 3.56974
INFO:root:Training epoch 5, Iteration 150, Loss: 3.48143
INFO:root:Training epoch 5, Iteration 180, Loss: 3.53917
INFO:root:Training epoch 5, Iteration 210, Loss: 3.42635
INFO:root:Training epoch 5, Iteration 240, Loss: 3.61217
INFO:root:Training epoch 5, Iteration 270, Loss: 3.66413
INFO:root:Training epoch 5, Iteration 300, Loss: 3.37192
INFO:root:Training epoch 5, Iteration 330, Loss: 3.47926
INFO:root:Training epoch 5, Iteration 360, Loss: 3.55290
INFO:root:Training epoch 5, Iteration 390, Loss: 3.45774
INFO:root:Training epoch 5, Iteration 420, Loss: 3.47220
INFO:root:Training epoch 5, Iteration 450, Loss: 3.57495
INFO:root:Training epoch 5, Iteration 480, Loss: 3.40851
INFO:root:Training epoch 5, Iteration 510, Loss: 3.50566
INFO:root:Training epoch 5, Iteration 540, Loss: 3.44367
INFO:root:Training epoch 5, Iteration 570, Loss: 3.38177
INFO:root:Training epoch 5, Iteration 600, Loss: 3.50319
INFO:root:Training epoch 5, Iteration 630, Loss: 3.44042
INFO:root:Training epoch 5, Iteration 660, Loss: 3.45478
INFO:root:Training epoch 5, Iteration 690, Loss: 3.64595
INFO:root:Training epoch 5, Iteration 720, Loss: 3.61875
INFO:root:Training epoch 5, Iteration 750, Loss: 3.41226
INFO:root:Training epoch 5, Iteration 780, Loss: 3.54106
INFO:root:Validation iteration 1, Loss: 4.46405
INFO:root:Validation iteration 10, Loss: 4.86947
INFO:root:Validation iteration 20, Loss: 4.69500
INFO:root:Validation iteration 30, Loss: 189.31534
INFO:root:Validation iteration 40, Loss: 599.18442
INFO:root:Validation iteration 50, Loss: 734.82587
INFO:root:Validation iteration 60, Loss: 4.97883
INFO:root:Validation iteration 70, Loss: 4.70879
INFO:root:Validation iteration 80, Loss: 4.71127
INFO:root:Validation iteration 90, Loss: 4.73994
INFO:root:Validation iteration 100, Loss: 10.99061
INFO:root:Validation iteration 110, Loss: 4.82039
INFO:root:Validation iteration 120, Loss: 4.54036
INFO:root:Validation iteration 130, Loss: 2433.21083
INFO:root:Validation iteration 140, Loss: 4.93003
INFO:root:Validation iteration 150, Loss: 4.63992
INFO:root:Validation iteration 160, Loss: 4.75731
INFO:root:Validation iteration 170, Loss: 4.84746
INFO:root:Validation iteration 180, Loss: 1163.33444
INFO:root:Validation iteration 190, Loss: 4.67044
INFO:root:Validation iteration 200, Loss: 4.65662
INFO:root:Validation iteration 210, Loss: 4.73635
INFO:root:Validation iteration 220, Loss: 5.98475
INFO:root:Validation iteration 230, Loss: 4.75722
INFO:root:Validation iteration 240, Loss: 5.29857
INFO:root:Validation iteration 250, Loss: 4.70382
INFO:root:Validation iteration 260, Loss: 1960.06633
INFO:root:End of Epoch 5
INFO:root:Training loss: 3.502
INFO:root:Validation accuracy: 0.037, Validation loss: 270.14613
INFO:root:Best validation accuracy: 0.170 at epoch 4
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.30711
INFO:root:Validation iteration 10, Loss: 5.82668
INFO:root:Validation iteration 20, Loss: 4.56259
INFO:root:Validation iteration 30, Loss: 5.72150
INFO:root:Validation iteration 40, Loss: 4.17317
INFO:root:Validation iteration 50, Loss: 3.78052
INFO:root:Validation iteration 60, Loss: 3.40966
INFO:root:Validation iteration 70, Loss: 5.21492
INFO:root:Validation iteration 80, Loss: 3.87503
INFO:root:Validation iteration 90, Loss: 3.59661
INFO:root:Validation iteration 100, Loss: 3.63436
INFO:root:Validation iteration 110, Loss: 4.56097
INFO:root:Validation iteration 120, Loss: 3.62145
INFO:root:Validation iteration 130, Loss: 3.50509
INFO:root:Validation iteration 140, Loss: 4.65724
INFO:root:Validation iteration 150, Loss: 3.73047
INFO:root:Validation iteration 160, Loss: 3.64173
INFO:root:Validation iteration 170, Loss: 3.51903
INFO:root:Validation iteration 180, Loss: 4.02417
INFO:root:Validation iteration 190, Loss: 3.77145
INFO:root:Validation iteration 200, Loss: 4.00635
INFO:root:Validation iteration 210, Loss: 3.83291
INFO:root:Validation iteration 220, Loss: 3.70770
INFO:root:Validation iteration 230, Loss: 3.54642
INFO:root:Validation iteration 240, Loss: 3.73567
INFO:root:Validation iteration 250, Loss: 3.71829
INFO:root:Validation iteration 260, Loss: 3.71652
Test accuracy: 0.173, Test loss: 4.14661
INFO:root:Saving results...
INFO:root:Done!
"""

string22 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', test_root='./data/kaggle_testset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.', trained_model_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/temp/best_model_5.pth', predictions_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/predictions.csv'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size_model=32, batch_size_stats=128, train_split_size=0.75), 'train': TrainConfig(num_epochs=10, train_log_frequency=20, val_log_frequency=8, train_accuracy=False, num_classes=161, lr=0.0001, momentum=0.9, weight_decay=1e-05, scheduler_step_size=5, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False, save_predictions=False, resume_training=False), 'model': ModelConfig(backbone_type=None, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/100
INFO:root:Processing batch 2/100
INFO:root:Processing batch 3/100
INFO:root:Processing batch 4/100
INFO:root:Processing batch 5/100
INFO:root:Processing batch 6/100
INFO:root:Processing batch 7/100
INFO:root:Processing batch 8/100
INFO:root:Processing batch 9/100
INFO:root:Processing batch 10/100
INFO:root:Processing batch 11/100
INFO:root:Processing batch 12/100
INFO:root:Processing batch 13/100
INFO:root:Processing batch 14/100
INFO:root:Processing batch 15/100
INFO:root:Processing batch 16/100
INFO:root:Processing batch 17/100
INFO:root:Processing batch 18/100
INFO:root:Processing batch 19/100
INFO:root:Processing batch 20/100
INFO:root:Processing batch 21/100
INFO:root:Processing batch 22/100
INFO:root:Processing batch 23/100
INFO:root:Processing batch 24/100
INFO:root:Processing batch 25/100
INFO:root:Processing batch 26/100
INFO:root:Processing batch 27/100
INFO:root:Processing batch 28/100
INFO:root:Processing batch 29/100
INFO:root:Processing batch 30/100
INFO:root:Processing batch 31/100
INFO:root:Processing batch 32/100
INFO:root:Processing batch 33/100
INFO:root:Processing batch 34/100
INFO:root:Processing batch 35/100
INFO:root:Processing batch 36/100
INFO:root:Processing batch 37/100
INFO:root:Processing batch 38/100
INFO:root:Processing batch 39/100
INFO:root:Processing batch 40/100
INFO:root:Processing batch 41/100
INFO:root:Processing batch 42/100
INFO:root:Processing batch 43/100
INFO:root:Processing batch 44/100
INFO:root:Processing batch 45/100
INFO:root:Processing batch 46/100
INFO:root:Processing batch 47/100
INFO:root:Processing batch 48/100
INFO:root:Processing batch 49/100
INFO:root:Processing batch 50/100
INFO:root:Processing batch 51/100
INFO:root:Processing batch 52/100
INFO:root:Processing batch 53/100
INFO:root:Processing batch 54/100
INFO:root:Processing batch 55/100
INFO:root:Processing batch 56/100
INFO:root:Processing batch 57/100
INFO:root:Processing batch 58/100
INFO:root:Processing batch 59/100
INFO:root:Processing batch 60/100
INFO:root:Processing batch 61/100
INFO:root:Processing batch 62/100
INFO:root:Processing batch 63/100
INFO:root:Processing batch 64/100
INFO:root:Processing batch 65/100
INFO:root:Processing batch 66/100
INFO:root:Processing batch 67/100
INFO:root:Processing batch 68/100
INFO:root:Processing batch 69/100
INFO:root:Processing batch 70/100
INFO:root:Processing batch 71/100
INFO:root:Processing batch 72/100
INFO:root:Processing batch 73/100
INFO:root:Processing batch 74/100
INFO:root:Processing batch 75/100
INFO:root:Processing batch 76/100
INFO:root:Processing batch 77/100
INFO:root:Processing batch 78/100
INFO:root:Processing batch 79/100
INFO:root:Processing batch 80/100
INFO:root:Processing batch 81/100
INFO:root:Processing batch 82/100
INFO:root:Processing batch 83/100
INFO:root:Processing batch 84/100
INFO:root:Processing batch 85/100
INFO:root:Processing batch 86/100
INFO:root:Processing batch 87/100
INFO:root:Processing batch 88/100
INFO:root:Processing batch 89/100
INFO:root:Processing batch 90/100
INFO:root:Processing batch 91/100
INFO:root:Processing batch 92/100
INFO:root:Processing batch 93/100
INFO:root:Processing batch 94/100
INFO:root:Processing batch 95/100
INFO:root:Processing batch 96/100
INFO:root:Processing batch 97/100
INFO:root:Processing batch 98/100
INFO:root:Processing batch 99/100
INFO:root:Processing batch 100/100
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47481051087379456, 0.4196726083755493, 0.3590790629386902], 'std': [0.27919673919677734, 0.27405110001564026, 0.2634223699569702], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47481051087379456, 0.4196726083755493, 0.3590790629386902], std=[0.27919673919677734, 0.27405110001564026, 0.2634223699569702])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.13157
INFO:root:Training epoch 1, Iteration 20, Loss: 5.00722
INFO:root:Training epoch 1, Iteration 40, Loss: 4.85818
INFO:root:Training epoch 1, Iteration 60, Loss: 4.72759
INFO:root:Training epoch 1, Iteration 80, Loss: 4.65134
INFO:root:Training epoch 1, Iteration 100, Loss: 4.60024
INFO:root:Training epoch 1, Iteration 120, Loss: 4.56178
INFO:root:Training epoch 1, Iteration 140, Loss: 4.44807
INFO:root:Training epoch 1, Iteration 160, Loss: 4.40818
INFO:root:Training epoch 1, Iteration 180, Loss: 4.34177
INFO:root:Training epoch 1, Iteration 200, Loss: 4.35707
INFO:root:Training epoch 1, Iteration 220, Loss: 4.41345
INFO:root:Training epoch 1, Iteration 240, Loss: 4.43588
INFO:root:Training epoch 1, Iteration 260, Loss: 4.41507
INFO:root:Training epoch 1, Iteration 280, Loss: 4.31209
INFO:root:Training epoch 1, Iteration 300, Loss: 4.28791
INFO:root:Training epoch 1, Iteration 320, Loss: 4.22630
INFO:root:Training epoch 1, Iteration 340, Loss: 4.28651
INFO:root:Training epoch 1, Iteration 360, Loss: 4.21304
INFO:root:Training epoch 1, Iteration 380, Loss: 4.24118
INFO:root:Validation iteration 1, Loss: 4.56416
INFO:root:Validation iteration 8, Loss: 4.19113
INFO:root:Validation iteration 16, Loss: 4.10782
INFO:root:Validation iteration 24, Loss: 4.18710
INFO:root:Validation iteration 32, Loss: 4.09538
INFO:root:Validation iteration 40, Loss: 4.08281
INFO:root:Validation iteration 48, Loss: 4.16295
INFO:root:Validation iteration 56, Loss: 4.11415
INFO:root:Validation iteration 64, Loss: 4.04531
INFO:root:Validation iteration 72, Loss: 4.23686
INFO:root:Validation iteration 80, Loss: 4.20944
INFO:root:Validation iteration 88, Loss: 4.19115
INFO:root:Validation iteration 96, Loss: 4.05291
INFO:root:Validation iteration 104, Loss: 4.08705
INFO:root:Validation iteration 112, Loss: 4.18829
INFO:root:Validation iteration 120, Loss: 4.29779
INFO:root:Validation iteration 128, Loss: 4.11326
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.451
INFO:root:Validation accuracy: 0.073, Validation loss: 4.14887
INFO:root:Training epoch 2, Iteration 1, Loss: 4.07222
INFO:root:Training epoch 2, Iteration 20, Loss: 3.98067
INFO:root:Training epoch 2, Iteration 40, Loss: 4.08190
INFO:root:Training epoch 2, Iteration 60, Loss: 3.94592
INFO:root:Training epoch 2, Iteration 80, Loss: 4.07806
INFO:root:Training epoch 2, Iteration 100, Loss: 4.05022
INFO:root:Training epoch 2, Iteration 120, Loss: 4.04811
INFO:root:Training epoch 2, Iteration 140, Loss: 3.98376
INFO:root:Training epoch 2, Iteration 160, Loss: 4.05184
INFO:root:Training epoch 2, Iteration 180, Loss: 4.01750
INFO:root:Training epoch 2, Iteration 200, Loss: 4.03719
INFO:root:Training epoch 2, Iteration 220, Loss: 3.99572
INFO:root:Training epoch 2, Iteration 240, Loss: 3.92609
INFO:root:Training epoch 2, Iteration 260, Loss: 4.01337
INFO:root:Training epoch 2, Iteration 280, Loss: 3.90930
INFO:root:Training epoch 2, Iteration 300, Loss: 3.92801
INFO:root:Training epoch 2, Iteration 320, Loss: 3.89983
INFO:root:Training epoch 2, Iteration 340, Loss: 3.92235
INFO:root:Training epoch 2, Iteration 360, Loss: 3.91237
INFO:root:Training epoch 2, Iteration 380, Loss: 3.91129
INFO:root:Validation iteration 1, Loss: 4.18599
INFO:root:Validation iteration 8, Loss: 3.94798
INFO:root:Validation iteration 16, Loss: 3.77360
INFO:root:Validation iteration 24, Loss: 3.90937
INFO:root:Validation iteration 32, Loss: 3.86648
INFO:root:Validation iteration 40, Loss: 3.85201
INFO:root:Validation iteration 48, Loss: 3.79247
INFO:root:Validation iteration 56, Loss: 3.88058
INFO:root:Validation iteration 64, Loss: 3.77755
INFO:root:Validation iteration 72, Loss: 3.99247
INFO:root:Validation iteration 80, Loss: 3.89611
INFO:root:Validation iteration 88, Loss: 3.88628
INFO:root:Validation iteration 96, Loss: 3.77299
INFO:root:Validation iteration 104, Loss: 3.82305
INFO:root:Validation iteration 112, Loss: 3.92317
INFO:root:Validation iteration 120, Loss: 3.97733
INFO:root:Validation iteration 128, Loss: 3.79355
INFO:root:End of Epoch 2
INFO:root:Training loss: 3.976
INFO:root:Validation accuracy: 0.112, Validation loss: 3.86955
INFO:root:Training epoch 3, Iteration 1, Loss: 3.73496
INFO:root:Training epoch 3, Iteration 20, Loss: 3.66674
INFO:root:Training epoch 3, Iteration 40, Loss: 3.66946
INFO:root:Training epoch 3, Iteration 60, Loss: 3.84267
INFO:root:Training epoch 3, Iteration 80, Loss: 3.83965
INFO:root:Training epoch 3, Iteration 100, Loss: 3.74947
INFO:root:Training epoch 3, Iteration 120, Loss: 3.64560
INFO:root:Training epoch 3, Iteration 140, Loss: 3.87659
INFO:root:Training epoch 3, Iteration 160, Loss: 3.73329
INFO:root:Training epoch 3, Iteration 180, Loss: 3.76076
INFO:root:Training epoch 3, Iteration 200, Loss: 3.75974
INFO:root:Training epoch 3, Iteration 220, Loss: 3.77274
INFO:root:Training epoch 3, Iteration 240, Loss: 3.68884
INFO:root:Training epoch 3, Iteration 260, Loss: 3.75475
INFO:root:Training epoch 3, Iteration 280, Loss: 3.58868
INFO:root:Training epoch 3, Iteration 300, Loss: 3.64243
INFO:root:Training epoch 3, Iteration 320, Loss: 3.64248
INFO:root:Training epoch 3, Iteration 340, Loss: 3.62106
INFO:root:Training epoch 3, Iteration 360, Loss: 3.60810
INFO:root:Training epoch 3, Iteration 380, Loss: 3.62359
INFO:root:Validation iteration 1, Loss: 4.12171
INFO:root:Validation iteration 8, Loss: 3.87258
INFO:root:Validation iteration 16, Loss: 3.64199
INFO:root:Validation iteration 24, Loss: 3.78426
INFO:root:Validation iteration 32, Loss: 3.64844
INFO:root:Validation iteration 40, Loss: 3.67433
INFO:root:Validation iteration 48, Loss: 3.78621
INFO:root:Validation iteration 56, Loss: 3.65413
INFO:root:Validation iteration 64, Loss: 3.66696
INFO:root:Validation iteration 72, Loss: 3.71724
INFO:root:Validation iteration 80, Loss: 3.60300
INFO:root:Validation iteration 88, Loss: 3.79811
INFO:root:Validation iteration 96, Loss: 3.61920
INFO:root:Validation iteration 104, Loss: 3.58713
INFO:root:Validation iteration 112, Loss: 3.73756
INFO:root:Validation iteration 120, Loss: 3.71355
INFO:root:Validation iteration 128, Loss: 3.62389
INFO:root:End of Epoch 3
INFO:root:Training loss: 3.712
INFO:root:Validation accuracy: 0.150, Validation loss: 3.69760
INFO:root:Training epoch 4, Iteration 1, Loss: 3.29687
INFO:root:Training epoch 4, Iteration 20, Loss: 3.45121
INFO:root:Training epoch 4, Iteration 40, Loss: 3.54051
INFO:root:Training epoch 4, Iteration 60, Loss: 3.50947
INFO:root:Training epoch 4, Iteration 80, Loss: 3.34938
INFO:root:Training epoch 4, Iteration 100, Loss: 3.50765
INFO:root:Training epoch 4, Iteration 120, Loss: 3.53022
INFO:root:Training epoch 4, Iteration 140, Loss: 3.62782
INFO:root:Training epoch 4, Iteration 160, Loss: 3.54425
INFO:root:Training epoch 4, Iteration 180, Loss: 3.47605
INFO:root:Training epoch 4, Iteration 200, Loss: 3.46426
INFO:root:Training epoch 4, Iteration 220, Loss: 3.58517
INFO:root:Training epoch 4, Iteration 240, Loss: 3.54141
INFO:root:Training epoch 4, Iteration 260, Loss: 3.51029
INFO:root:Training epoch 4, Iteration 280, Loss: 3.50274
INFO:root:Training epoch 4, Iteration 300, Loss: 3.46677
INFO:root:Training epoch 4, Iteration 320, Loss: 3.50146
INFO:root:Training epoch 4, Iteration 340, Loss: 3.54782
INFO:root:Training epoch 4, Iteration 360, Loss: 3.45733
INFO:root:Training epoch 4, Iteration 380, Loss: 3.54907
INFO:root:Validation iteration 1, Loss: 4.00364
INFO:root:Validation iteration 8, Loss: 3.70447
INFO:root:Validation iteration 16, Loss: 3.50016
INFO:root:Validation iteration 24, Loss: 3.58950
INFO:root:Validation iteration 32, Loss: 3.45912
INFO:root:Validation iteration 40, Loss: 3.58050
INFO:root:Validation iteration 48, Loss: 3.54850
INFO:root:Validation iteration 56, Loss: 3.57174
INFO:root:Validation iteration 64, Loss: 3.45630
INFO:root:Validation iteration 72, Loss: 3.58639
INFO:root:Validation iteration 80, Loss: 3.50334
INFO:root:Validation iteration 88, Loss: 3.64624
INFO:root:Validation iteration 96, Loss: 3.44606
INFO:root:Validation iteration 104, Loss: 3.41044
INFO:root:Validation iteration 112, Loss: 3.60798
INFO:root:Validation iteration 120, Loss: 3.57944
INFO:root:Validation iteration 128, Loss: 3.54926
INFO:root:End of Epoch 4
INFO:root:Training loss: 3.508
INFO:root:Validation accuracy: 0.187, Validation loss: 3.54995
INFO:root:Training epoch 5, Iteration 1, Loss: 3.33407
INFO:root:Training epoch 5, Iteration 20, Loss: 3.31508
INFO:root:Training epoch 5, Iteration 40, Loss: 3.25290
INFO:root:Training epoch 5, Iteration 60, Loss: 3.37293
INFO:root:Training epoch 5, Iteration 80, Loss: 3.48838
INFO:root:Training epoch 5, Iteration 100, Loss: 3.28982
INFO:root:Training epoch 5, Iteration 120, Loss: 3.43784
INFO:root:Training epoch 5, Iteration 140, Loss: 3.35442
INFO:root:Training epoch 5, Iteration 160, Loss: 3.38287
INFO:root:Training epoch 5, Iteration 180, Loss: 3.32092
INFO:root:Training epoch 5, Iteration 200, Loss: 3.37014
INFO:root:Training epoch 5, Iteration 220, Loss: 3.39618
INFO:root:Training epoch 5, Iteration 240, Loss: 3.41766
INFO:root:Training epoch 5, Iteration 260, Loss: 3.26397
INFO:root:Training epoch 5, Iteration 280, Loss: 3.40709
INFO:root:Training epoch 5, Iteration 300, Loss: 3.33120
INFO:root:Training epoch 5, Iteration 320, Loss: 3.43706
INFO:root:Training epoch 5, Iteration 340, Loss: 3.34669
INFO:root:Training epoch 5, Iteration 360, Loss: 3.24255
INFO:root:Training epoch 5, Iteration 380, Loss: 3.25329
INFO:root:Validation iteration 1, Loss: 3.81348
INFO:root:Validation iteration 8, Loss: 3.60840
INFO:root:Validation iteration 16, Loss: 3.39922
INFO:root:Validation iteration 24, Loss: 3.55939
INFO:root:Validation iteration 32, Loss: 3.43094
INFO:root:Validation iteration 40, Loss: 3.55560
INFO:root:Validation iteration 48, Loss: 3.54355
INFO:root:Validation iteration 56, Loss: 3.57398
INFO:root:Validation iteration 64, Loss: 3.34227
INFO:root:Validation iteration 72, Loss: 3.48294
INFO:root:Validation iteration 80, Loss: 3.43156
INFO:root:Validation iteration 88, Loss: 3.41381
INFO:root:Validation iteration 96, Loss: 3.37617
INFO:root:Validation iteration 104, Loss: 3.28484
INFO:root:Validation iteration 112, Loss: 3.58024
INFO:root:Validation iteration 120, Loss: 3.54608
INFO:root:Validation iteration 128, Loss: 3.41982
INFO:root:End of Epoch 5
INFO:root:Training loss: 3.343
INFO:root:Validation accuracy: 0.199, Validation loss: 3.47985
INFO:root:Training epoch 6, Iteration 1, Loss: 3.07102
INFO:root:Training epoch 6, Iteration 20, Loss: 3.18946
INFO:root:Training epoch 6, Iteration 40, Loss: 3.08566
INFO:root:Training epoch 6, Iteration 60, Loss: 2.98121
INFO:root:Training epoch 6, Iteration 80, Loss: 3.06470
INFO:root:Training epoch 6, Iteration 100, Loss: 3.07541
INFO:root:Training epoch 6, Iteration 120, Loss: 3.10594
INFO:root:Training epoch 6, Iteration 140, Loss: 3.09460
INFO:root:Training epoch 6, Iteration 160, Loss: 2.95121
INFO:root:Training epoch 6, Iteration 180, Loss: 3.03298
INFO:root:Training epoch 6, Iteration 200, Loss: 3.00110
INFO:root:Training epoch 6, Iteration 220, Loss: 3.07742
INFO:root:Training epoch 6, Iteration 240, Loss: 3.02852
INFO:root:Training epoch 6, Iteration 260, Loss: 3.01560
INFO:root:Training epoch 6, Iteration 280, Loss: 2.99396
INFO:root:Training epoch 6, Iteration 300, Loss: 3.03937
INFO:root:Training epoch 6, Iteration 320, Loss: 3.17006
INFO:root:Training epoch 6, Iteration 340, Loss: 3.12309
INFO:root:Training epoch 6, Iteration 360, Loss: 3.02299
INFO:root:Training epoch 6, Iteration 380, Loss: 3.01755
INFO:root:Validation iteration 1, Loss: 3.58393
INFO:root:Validation iteration 8, Loss: 3.35775
INFO:root:Validation iteration 16, Loss: 3.14670
INFO:root:Validation iteration 24, Loss: 3.30797
INFO:root:Validation iteration 32, Loss: 3.17826
INFO:root:Validation iteration 40, Loss: 3.28985
INFO:root:Validation iteration 48, Loss: 3.26944
INFO:root:Validation iteration 56, Loss: 3.28704
INFO:root:Validation iteration 64, Loss: 3.14140
INFO:root:Validation iteration 72, Loss: 3.30563
INFO:root:Validation iteration 80, Loss: 3.19694
INFO:root:Validation iteration 88, Loss: 3.20447
INFO:root:Validation iteration 96, Loss: 3.11025
INFO:root:Validation iteration 104, Loss: 3.02781
INFO:root:Validation iteration 112, Loss: 3.32444
INFO:root:Validation iteration 120, Loss: 3.21518
INFO:root:Validation iteration 128, Loss: 3.15223
INFO:root:End of Epoch 6
INFO:root:Training loss: 3.055
INFO:root:Validation accuracy: 0.238, Validation loss: 3.23021
INFO:root:Training epoch 7, Iteration 1, Loss: 3.56950
INFO:root:Training epoch 7, Iteration 20, Loss: 2.95282
INFO:root:Training epoch 7, Iteration 40, Loss: 2.91926
INFO:root:Training epoch 7, Iteration 60, Loss: 2.96245
INFO:root:Training epoch 7, Iteration 80, Loss: 2.91956
INFO:root:Training epoch 7, Iteration 100, Loss: 3.01688
INFO:root:Training epoch 7, Iteration 120, Loss: 3.03091
INFO:root:Training epoch 7, Iteration 140, Loss: 2.97243
INFO:root:Training epoch 7, Iteration 160, Loss: 2.93534
INFO:root:Training epoch 7, Iteration 180, Loss: 2.97248
INFO:root:Training epoch 7, Iteration 200, Loss: 2.92744
INFO:root:Training epoch 7, Iteration 220, Loss: 3.00604
INFO:root:Training epoch 7, Iteration 240, Loss: 2.95380
INFO:root:Training epoch 7, Iteration 260, Loss: 2.89384
INFO:root:Training epoch 7, Iteration 280, Loss: 2.96354
INFO:root:Training epoch 7, Iteration 300, Loss: 3.00225
INFO:root:Training epoch 7, Iteration 320, Loss: 2.95032
INFO:root:Training epoch 7, Iteration 340, Loss: 3.06101
INFO:root:Training epoch 7, Iteration 360, Loss: 2.91598
INFO:root:Training epoch 7, Iteration 380, Loss: 2.97013
INFO:root:Validation iteration 1, Loss: 3.56131
INFO:root:Validation iteration 8, Loss: 3.30880
INFO:root:Validation iteration 16, Loss: 3.07867
INFO:root:Validation iteration 24, Loss: 3.21072
INFO:root:Validation iteration 32, Loss: 3.11466
INFO:root:Validation iteration 40, Loss: 3.23512
INFO:root:Validation iteration 48, Loss: 3.20404
INFO:root:Validation iteration 56, Loss: 3.19886
INFO:root:Validation iteration 64, Loss: 3.09749
INFO:root:Validation iteration 72, Loss: 3.28970
INFO:root:Validation iteration 80, Loss: 3.13619
INFO:root:Validation iteration 88, Loss: 3.15526
INFO:root:Validation iteration 96, Loss: 3.09495
INFO:root:Validation iteration 104, Loss: 3.02030
INFO:root:Validation iteration 112, Loss: 3.24111
INFO:root:Validation iteration 120, Loss: 3.16487
INFO:root:Validation iteration 128, Loss: 3.11892
INFO:root:End of Epoch 7
INFO:root:Training loss: 2.966
INFO:root:Validation accuracy: 0.249, Validation loss: 3.17702
INFO:root:Training epoch 8, Iteration 1, Loss: 3.09027
INFO:root:Training epoch 8, Iteration 20, Loss: 3.05122
INFO:root:Training epoch 8, Iteration 40, Loss: 2.83651
INFO:root:Training epoch 8, Iteration 60, Loss: 3.02998
INFO:root:Training epoch 8, Iteration 80, Loss: 2.95373
INFO:root:Training epoch 8, Iteration 100, Loss: 2.88633
INFO:root:Training epoch 8, Iteration 120, Loss: 2.86835
INFO:root:Training epoch 8, Iteration 140, Loss: 2.85219
INFO:root:Training epoch 8, Iteration 160, Loss: 2.91024
INFO:root:Training epoch 8, Iteration 180, Loss: 3.07910
INFO:root:Training epoch 8, Iteration 200, Loss: 2.90573
INFO:root:Training epoch 8, Iteration 220, Loss: 2.89052
INFO:root:Training epoch 8, Iteration 240, Loss: 2.87608
INFO:root:Training epoch 8, Iteration 260, Loss: 2.91838
INFO:root:Training epoch 8, Iteration 280, Loss: 2.92323
INFO:root:Training epoch 8, Iteration 300, Loss: 2.95817
INFO:root:Training epoch 8, Iteration 320, Loss: 2.96265
INFO:root:Training epoch 8, Iteration 340, Loss: 2.94525
INFO:root:Training epoch 8, Iteration 360, Loss: 2.94937
INFO:root:Training epoch 8, Iteration 380, Loss: 2.99539
INFO:root:Validation iteration 1, Loss: 3.53868
INFO:root:Validation iteration 8, Loss: 3.29785
INFO:root:Validation iteration 16, Loss: 3.05635
INFO:root:Validation iteration 24, Loss: 3.20544
INFO:root:Validation iteration 32, Loss: 3.14220
INFO:root:Validation iteration 40, Loss: 3.22523
INFO:root:Validation iteration 48, Loss: 3.18211
INFO:root:Validation iteration 56, Loss: 3.19879
INFO:root:Validation iteration 64, Loss: 3.08059
INFO:root:Validation iteration 72, Loss: 3.25318
INFO:root:Validation iteration 80, Loss: 3.07141
INFO:root:Validation iteration 88, Loss: 3.08855
INFO:root:Validation iteration 96, Loss: 3.04722
INFO:root:Validation iteration 104, Loss: 3.01852
INFO:root:Validation iteration 112, Loss: 3.19693
INFO:root:Validation iteration 120, Loss: 3.14255
INFO:root:Validation iteration 128, Loss: 3.10256
INFO:root:End of Epoch 8
INFO:root:Training loss: 2.940
INFO:root:Validation accuracy: 0.252, Validation loss: 3.15437
INFO:root:Training epoch 9, Iteration 1, Loss: 2.51857
INFO:root:Training epoch 9, Iteration 20, Loss: 2.82051
INFO:root:Training epoch 9, Iteration 40, Loss: 2.97073
INFO:root:Training epoch 9, Iteration 60, Loss: 2.90006
INFO:root:Training epoch 9, Iteration 80, Loss: 2.83032
INFO:root:Training epoch 9, Iteration 100, Loss: 2.86697
INFO:root:Training epoch 9, Iteration 120, Loss: 2.99322
INFO:root:Training epoch 9, Iteration 140, Loss: 2.91076
INFO:root:Training epoch 9, Iteration 160, Loss: 2.89492
INFO:root:Training epoch 9, Iteration 180, Loss: 2.87847
INFO:root:Training epoch 9, Iteration 200, Loss: 2.85437
INFO:root:Training epoch 9, Iteration 220, Loss: 2.92310
INFO:root:Training epoch 9, Iteration 240, Loss: 2.93040
INFO:root:Training epoch 9, Iteration 260, Loss: 2.81715
INFO:root:Training epoch 9, Iteration 280, Loss: 2.98680
INFO:root:Training epoch 9, Iteration 300, Loss: 2.87095
INFO:root:Training epoch 9, Iteration 320, Loss: 2.80317
INFO:root:Training epoch 9, Iteration 340, Loss: 2.76928
INFO:root:Training epoch 9, Iteration 360, Loss: 2.81134
INFO:root:Training epoch 9, Iteration 380, Loss: 2.80401
INFO:root:Validation iteration 1, Loss: 3.45692
INFO:root:Validation iteration 8, Loss: 3.25555
INFO:root:Validation iteration 16, Loss: 3.00740
INFO:root:Validation iteration 24, Loss: 3.17072
INFO:root:Validation iteration 32, Loss: 3.08199
INFO:root:Validation iteration 40, Loss: 3.21975
INFO:root:Validation iteration 48, Loss: 3.12564
INFO:root:Validation iteration 56, Loss: 3.13432
INFO:root:Validation iteration 64, Loss: 3.08163
INFO:root:Validation iteration 72, Loss: 3.21321
INFO:root:Validation iteration 80, Loss: 3.01111
INFO:root:Validation iteration 88, Loss: 3.14199
INFO:root:Validation iteration 96, Loss: 3.00852
INFO:root:Validation iteration 104, Loss: 2.94377
INFO:root:Validation iteration 112, Loss: 3.18448
INFO:root:Validation iteration 120, Loss: 3.15607
INFO:root:Validation iteration 128, Loss: 3.09709
INFO:root:End of Epoch 9
INFO:root:Training loss: 2.879
INFO:root:Validation accuracy: 0.260, Validation loss: 3.12453
INFO:root:Training epoch 10, Iteration 1, Loss: 2.99960
INFO:root:Training epoch 10, Iteration 20, Loss: 2.86006
INFO:root:Training epoch 10, Iteration 40, Loss: 2.85415
INFO:root:Training epoch 10, Iteration 60, Loss: 2.85010
INFO:root:Training epoch 10, Iteration 80, Loss: 2.77082
INFO:root:Training epoch 10, Iteration 100, Loss: 2.85220
INFO:root:Training epoch 10, Iteration 120, Loss: 2.79680
INFO:root:Training epoch 10, Iteration 140, Loss: 2.86876
INFO:root:Training epoch 10, Iteration 160, Loss: 2.87812
INFO:root:Training epoch 10, Iteration 180, Loss: 2.89634
INFO:root:Training epoch 10, Iteration 200, Loss: 2.90780
INFO:root:Training epoch 10, Iteration 220, Loss: 2.84317
INFO:root:Training epoch 10, Iteration 240, Loss: 2.91352
INFO:root:Training epoch 10, Iteration 260, Loss: 2.91002
INFO:root:Training epoch 10, Iteration 280, Loss: 2.82115
INFO:root:Training epoch 10, Iteration 300, Loss: 2.80927
INFO:root:Training epoch 10, Iteration 320, Loss: 2.72909
INFO:root:Training epoch 10, Iteration 340, Loss: 2.90900
INFO:root:Training epoch 10, Iteration 360, Loss: 2.83563
INFO:root:Training epoch 10, Iteration 380, Loss: 2.84798
INFO:root:Validation iteration 1, Loss: 3.52933
INFO:root:Validation iteration 8, Loss: 3.27232
INFO:root:Validation iteration 16, Loss: 2.98526
INFO:root:Validation iteration 24, Loss: 3.17551
INFO:root:Validation iteration 32, Loss: 3.08808
INFO:root:Validation iteration 40, Loss: 3.13546
INFO:root:Validation iteration 48, Loss: 3.12477
INFO:root:Validation iteration 56, Loss: 3.13270
INFO:root:Validation iteration 64, Loss: 3.02142
INFO:root:Validation iteration 72, Loss: 3.22391
INFO:root:Validation iteration 80, Loss: 3.02239
INFO:root:Validation iteration 88, Loss: 3.07392
INFO:root:Validation iteration 96, Loss: 3.02383
INFO:root:Validation iteration 104, Loss: 2.95703
INFO:root:Validation iteration 112, Loss: 3.16861
INFO:root:Validation iteration 120, Loss: 3.07133
INFO:root:Validation iteration 128, Loss: 3.06405
INFO:root:End of Epoch 10
INFO:root:Training loss: 2.848
INFO:root:Validation accuracy: 0.263, Validation loss: 3.10456
INFO:root:Best validation accuracy: 0.263 at epoch 10
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.10640
INFO:root:Validation iteration 8, Loss: 3.38972
INFO:root:Validation iteration 16, Loss: 3.26420
INFO:root:Validation iteration 24, Loss: 3.15254
INFO:root:Validation iteration 32, Loss: 3.00405
INFO:root:Validation iteration 40, Loss: 3.18460
INFO:root:Validation iteration 48, Loss: 3.16306
INFO:root:Validation iteration 56, Loss: 2.92109
INFO:root:Validation iteration 64, Loss: 2.94364
INFO:root:Validation iteration 72, Loss: 3.13434
INFO:root:Validation iteration 80, Loss: 2.89046
INFO:root:Validation iteration 88, Loss: 3.27014
INFO:root:Validation iteration 96, Loss: 3.00102
INFO:root:Validation iteration 104, Loss: 3.13727
INFO:root:Validation iteration 112, Loss: 3.17901
INFO:root:Validation iteration 120, Loss: 3.20639
INFO:root:Validation iteration 128, Loss: 3.17878
Test accuracy: 0.258, Test loss: 3.12189
INFO:root:Saving results...
INFO:root:Done!
"""

string23 = """
INFO:root:{'path': PathConfig(default_root='./data/artist_dataset', test_root='./data/kaggle_testset', stats_file='./scripts/stats/stats.json', norm_stats_file='./temp/norm_stats.json', best_model_path='./temp/best_model', results_root='.', trained_model_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/temp/best_model_5.pth', predictions_path='/content/drive/MyDrive/mlvm_shared/20241230_225438/predictions.csv'), 'env': EnvConfig(device='cuda', num_workers=2), 'data': DataConfig(pretrained_stats=False, resize_dim=512, crop_dim=512, aug_probs=(0.2, 0.2, 0.2, 0.5), aug_mask=(True, True, True, True), augment=False, reduce_factor=1.0, batch_size_model=16, batch_size_stats=128, train_split_size=0.75), 'train': TrainConfig(num_epochs=5, train_log_frequency=30, val_log_frequency=10, train_accuracy=False, num_classes=161, lr=1e-05, momentum=0.9, weight_decay=1e-05, scheduler_step_size=10, scheduler_gamma=0.1, criterion='cross_entropy', optimizer='adam', scheduler='step_lr', top_k=5, sanity_check=False, save_models=True, train_only=False, inference_only=False, save_predictions=False, resume_training=False), 'model': ModelConfig(backbone_type=<BackboneType.RESNET18: 'resnet18'>, use_handcrafted=False, precision=32), 'hog': HOGConfig(downsample_size=256, crop_size=224, channel_coefficients=(0.2989, 0.587, 0.114), orientations=9, pixels_per_cell=74, cells_per_block=1, transform_sqrt=False, feature_vector=True, normalization='L2-Hys')}
INFO:root:Processing batch 1/100
INFO:root:Processing batch 2/100
INFO:root:Processing batch 3/100
INFO:root:Processing batch 4/100
INFO:root:Processing batch 5/100
INFO:root:Processing batch 6/100
INFO:root:Processing batch 7/100
INFO:root:Processing batch 8/100
INFO:root:Processing batch 9/100
INFO:root:Processing batch 10/100
INFO:root:Processing batch 11/100
INFO:root:Processing batch 12/100
INFO:root:Processing batch 13/100
INFO:root:Processing batch 14/100
INFO:root:Processing batch 15/100
INFO:root:Processing batch 16/100
INFO:root:Processing batch 17/100
INFO:root:Processing batch 18/100
INFO:root:Processing batch 19/100
INFO:root:Processing batch 20/100
INFO:root:Processing batch 21/100
INFO:root:Processing batch 22/100
INFO:root:Processing batch 23/100
INFO:root:Processing batch 24/100
INFO:root:Processing batch 25/100
INFO:root:Processing batch 26/100
INFO:root:Processing batch 27/100
INFO:root:Processing batch 28/100
INFO:root:Processing batch 29/100
INFO:root:Processing batch 30/100
INFO:root:Processing batch 31/100
INFO:root:Processing batch 32/100
INFO:root:Processing batch 33/100
INFO:root:Processing batch 34/100
INFO:root:Processing batch 35/100
INFO:root:Processing batch 36/100
INFO:root:Processing batch 37/100
INFO:root:Processing batch 38/100
INFO:root:Processing batch 39/100
INFO:root:Processing batch 40/100
INFO:root:Processing batch 41/100
INFO:root:Processing batch 42/100
INFO:root:Processing batch 43/100
INFO:root:Processing batch 44/100
INFO:root:Processing batch 45/100
INFO:root:Processing batch 46/100
INFO:root:Processing batch 47/100
INFO:root:Processing batch 48/100
INFO:root:Processing batch 49/100
INFO:root:Processing batch 50/100
INFO:root:Processing batch 51/100
INFO:root:Processing batch 52/100
INFO:root:Processing batch 53/100
INFO:root:Processing batch 54/100
INFO:root:Processing batch 55/100
INFO:root:Processing batch 56/100
INFO:root:Processing batch 57/100
INFO:root:Processing batch 58/100
INFO:root:Processing batch 59/100
INFO:root:Processing batch 60/100
INFO:root:Processing batch 61/100
INFO:root:Processing batch 62/100
INFO:root:Processing batch 63/100
INFO:root:Processing batch 64/100
INFO:root:Processing batch 65/100
INFO:root:Processing batch 66/100
INFO:root:Processing batch 67/100
INFO:root:Processing batch 68/100
INFO:root:Processing batch 69/100
INFO:root:Processing batch 70/100
INFO:root:Processing batch 71/100
INFO:root:Processing batch 72/100
INFO:root:Processing batch 73/100
INFO:root:Processing batch 74/100
INFO:root:Processing batch 75/100
INFO:root:Processing batch 76/100
INFO:root:Processing batch 77/100
INFO:root:Processing batch 78/100
INFO:root:Processing batch 79/100
INFO:root:Processing batch 80/100
INFO:root:Processing batch 81/100
INFO:root:Processing batch 82/100
INFO:root:Processing batch 83/100
INFO:root:Processing batch 84/100
INFO:root:Processing batch 85/100
INFO:root:Processing batch 86/100
INFO:root:Processing batch 87/100
INFO:root:Processing batch 88/100
INFO:root:Processing batch 89/100
INFO:root:Processing batch 90/100
INFO:root:Processing batch 91/100
INFO:root:Processing batch 92/100
INFO:root:Processing batch 93/100
INFO:root:Processing batch 94/100
INFO:root:Processing batch 95/100
INFO:root:Processing batch 96/100
INFO:root:Processing batch 97/100
INFO:root:Processing batch 98/100
INFO:root:Processing batch 99/100
INFO:root:Processing batch 100/100
INFO:root:{'type': 'model', 'keys': ['train', 'eval', 'aug'], 'mean': [0.47481051087379456, 0.4196726083755493, 0.3590790629386902], 'std': [0.27919673919677734, 0.27405110001564026, 0.2634223699569702], 'transforms': {'train': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'eval': ['Resize(size=512, interpolation=bilinear, max_size=None, antialias=True)', 'CenterCrop(size=(512, 512))', 'ToTensor()'], 'aug': {'val': ['Normalize(mean=[0.47481051087379456, 0.4196726083755493, 0.3590790629386902], std=[0.27919673919677734, 0.27405110001564026, 0.2634223699569702])']}}}
INFO:root:Training setup...
INFO:root:Training...
INFO:root:No augmentation found, only normalization will be applied
INFO:root:Training epoch 1, Iteration 1, Loss: 5.21580
INFO:root:Training epoch 1, Iteration 30, Loss: 5.07530
INFO:root:Training epoch 1, Iteration 60, Loss: 5.02471
INFO:root:Training epoch 1, Iteration 90, Loss: 4.97205
INFO:root:Training epoch 1, Iteration 120, Loss: 4.94482
INFO:root:Training epoch 1, Iteration 150, Loss: 4.94950
INFO:root:Training epoch 1, Iteration 180, Loss: 4.88381
INFO:root:Training epoch 1, Iteration 210, Loss: 4.87005
INFO:root:Training epoch 1, Iteration 240, Loss: 4.87527
INFO:root:Training epoch 1, Iteration 270, Loss: 4.86163
INFO:root:Training epoch 1, Iteration 300, Loss: 4.84731
INFO:root:Training epoch 1, Iteration 330, Loss: 4.82440
INFO:root:Training epoch 1, Iteration 360, Loss: 4.78268
INFO:root:Training epoch 1, Iteration 390, Loss: 4.78093
INFO:root:Training epoch 1, Iteration 420, Loss: 4.71978
INFO:root:Training epoch 1, Iteration 450, Loss: 4.72226
INFO:root:Training epoch 1, Iteration 480, Loss: 4.73958
INFO:root:Training epoch 1, Iteration 510, Loss: 4.72062
INFO:root:Training epoch 1, Iteration 540, Loss: 4.74630
INFO:root:Training epoch 1, Iteration 570, Loss: 4.73949
INFO:root:Training epoch 1, Iteration 600, Loss: 4.69366
INFO:root:Training epoch 1, Iteration 630, Loss: 4.64558
INFO:root:Training epoch 1, Iteration 660, Loss: 4.67066
INFO:root:Training epoch 1, Iteration 690, Loss: 4.68207
INFO:root:Training epoch 1, Iteration 720, Loss: 4.67814
INFO:root:Training epoch 1, Iteration 750, Loss: 4.73923
INFO:root:Training epoch 1, Iteration 780, Loss: 4.65505
INFO:root:Validation iteration 1, Loss: 4.56780
INFO:root:Validation iteration 10, Loss: 4.68107
INFO:root:Validation iteration 20, Loss: 4.72854
INFO:root:Validation iteration 30, Loss: 4.70126
INFO:root:Validation iteration 40, Loss: 4.66966
INFO:root:Validation iteration 50, Loss: 4.59748
INFO:root:Validation iteration 60, Loss: 4.68749
INFO:root:Validation iteration 70, Loss: 4.65838
INFO:root:Validation iteration 80, Loss: 4.61794
INFO:root:Validation iteration 90, Loss: 4.56005
INFO:root:Validation iteration 100, Loss: 4.62510
INFO:root:Validation iteration 110, Loss: 4.80571
INFO:root:Validation iteration 120, Loss: 4.53335
INFO:root:Validation iteration 130, Loss: 4.65594
INFO:root:Validation iteration 140, Loss: 4.74884
INFO:root:Validation iteration 150, Loss: 4.59561
INFO:root:Validation iteration 160, Loss: 4.71940
INFO:root:Validation iteration 170, Loss: 4.65637
INFO:root:Validation iteration 180, Loss: 4.80162
INFO:root:Validation iteration 190, Loss: 4.63187
INFO:root:Validation iteration 200, Loss: 4.64817
INFO:root:Validation iteration 210, Loss: 4.65091
INFO:root:Validation iteration 220, Loss: 4.78589
INFO:root:Validation iteration 230, Loss: 4.73546
INFO:root:Validation iteration 240, Loss: 4.71813
INFO:root:Validation iteration 250, Loss: 4.71361
INFO:root:Validation iteration 260, Loss: 4.64227
INFO:root:End of Epoch 1
INFO:root:Training loss: 4.802
INFO:root:Validation accuracy: 0.026, Validation loss: 4.67758
INFO:root:Training epoch 2, Iteration 1, Loss: 4.76896
INFO:root:Training epoch 2, Iteration 30, Loss: 4.62627
INFO:root:Training epoch 2, Iteration 60, Loss: 4.74047
INFO:root:Training epoch 2, Iteration 90, Loss: 4.58566
INFO:root:Training epoch 2, Iteration 120, Loss: 4.61078
INFO:root:Training epoch 2, Iteration 150, Loss: 4.64268
INFO:root:Training epoch 2, Iteration 180, Loss: 4.66097
INFO:root:Training epoch 2, Iteration 210, Loss: 4.59292
INFO:root:Training epoch 2, Iteration 240, Loss: 4.60975
INFO:root:Training epoch 2, Iteration 270, Loss: 4.54612
INFO:root:Training epoch 2, Iteration 300, Loss: 4.52031
INFO:root:Training epoch 2, Iteration 330, Loss: 4.55109
INFO:root:Training epoch 2, Iteration 360, Loss: 4.53492
INFO:root:Training epoch 2, Iteration 390, Loss: 4.47592
INFO:root:Training epoch 2, Iteration 420, Loss: 4.57610
INFO:root:Training epoch 2, Iteration 450, Loss: 4.53628
INFO:root:Training epoch 2, Iteration 480, Loss: 4.49143
INFO:root:Training epoch 2, Iteration 510, Loss: 4.54418
INFO:root:Training epoch 2, Iteration 540, Loss: 4.46286
INFO:root:Training epoch 2, Iteration 570, Loss: 4.50756
INFO:root:Training epoch 2, Iteration 600, Loss: 4.64250
INFO:root:Training epoch 2, Iteration 630, Loss: 4.44664
INFO:root:Training epoch 2, Iteration 660, Loss: 4.48286
INFO:root:Training epoch 2, Iteration 690, Loss: 4.50380
INFO:root:Training epoch 2, Iteration 720, Loss: 4.51346
INFO:root:Training epoch 2, Iteration 750, Loss: 4.51316
INFO:root:Training epoch 2, Iteration 780, Loss: 4.45385
INFO:root:Validation iteration 1, Loss: 4.39380
INFO:root:Validation iteration 10, Loss: 4.44623
INFO:root:Validation iteration 20, Loss: 4.31963
INFO:root:Validation iteration 30, Loss: 4.48525
INFO:root:Validation iteration 40, Loss: 4.45282
INFO:root:Validation iteration 50, Loss: 4.35057
INFO:root:Validation iteration 60, Loss: 4.49189
INFO:root:Validation iteration 70, Loss: 4.37517
INFO:root:Validation iteration 80, Loss: 4.37095
INFO:root:Validation iteration 90, Loss: 4.26640
INFO:root:Validation iteration 100, Loss: 4.40644
INFO:root:Validation iteration 110, Loss: 4.59424
INFO:root:Validation iteration 120, Loss: 4.25594
INFO:root:Validation iteration 130, Loss: 4.40200
INFO:root:Validation iteration 140, Loss: 4.45930
INFO:root:Validation iteration 150, Loss: 4.42703
INFO:root:Validation iteration 160, Loss: 4.48114
INFO:root:Validation iteration 170, Loss: 4.35602
INFO:root:Validation iteration 180, Loss: 4.53611
INFO:root:Validation iteration 190, Loss: 4.39086
INFO:root:Validation iteration 200, Loss: 4.34520
INFO:root:Validation iteration 210, Loss: 4.41968
INFO:root:Validation iteration 220, Loss: 4.50079
INFO:root:Validation iteration 230, Loss: 4.46742
INFO:root:Validation iteration 240, Loss: 4.49525
INFO:root:Validation iteration 250, Loss: 4.49184
INFO:root:Validation iteration 260, Loss: 4.39276
INFO:root:End of Epoch 2
INFO:root:Training loss: 4.551
INFO:root:Validation accuracy: 0.041, Validation loss: 4.42552
INFO:root:Training epoch 3, Iteration 1, Loss: 4.65479
INFO:root:Training epoch 3, Iteration 30, Loss: 4.40445
INFO:root:Training epoch 3, Iteration 60, Loss: 4.40421
INFO:root:Training epoch 3, Iteration 90, Loss: 4.40449
INFO:root:Training epoch 3, Iteration 120, Loss: 4.39409
INFO:root:Training epoch 3, Iteration 150, Loss: 4.56452
INFO:root:Training epoch 3, Iteration 180, Loss: 4.44656
INFO:root:Training epoch 3, Iteration 210, Loss: 4.44027
INFO:root:Training epoch 3, Iteration 240, Loss: 4.43389
INFO:root:Training epoch 3, Iteration 270, Loss: 4.48208
INFO:root:Training epoch 3, Iteration 300, Loss: 4.51096
INFO:root:Training epoch 3, Iteration 330, Loss: 4.41823
INFO:root:Training epoch 3, Iteration 360, Loss: 4.42183
INFO:root:Training epoch 3, Iteration 390, Loss: 4.32950
INFO:root:Training epoch 3, Iteration 420, Loss: 4.40562
INFO:root:Training epoch 3, Iteration 450, Loss: 4.41577
INFO:root:Training epoch 3, Iteration 480, Loss: 4.45426
INFO:root:Training epoch 3, Iteration 510, Loss: 4.30901
INFO:root:Training epoch 3, Iteration 540, Loss: 4.25341
INFO:root:Training epoch 3, Iteration 570, Loss: 4.39612
INFO:root:Training epoch 3, Iteration 600, Loss: 4.32982
INFO:root:Training epoch 3, Iteration 630, Loss: 4.34610
INFO:root:Training epoch 3, Iteration 660, Loss: 4.41521
INFO:root:Training epoch 3, Iteration 690, Loss: 4.27398
INFO:root:Training epoch 3, Iteration 720, Loss: 4.41748
INFO:root:Training epoch 3, Iteration 750, Loss: 4.40519
INFO:root:Training epoch 3, Iteration 780, Loss: 4.25549
INFO:root:Validation iteration 1, Loss: 4.45889
INFO:root:Validation iteration 10, Loss: 4.32094
INFO:root:Validation iteration 20, Loss: 4.16862
INFO:root:Validation iteration 30, Loss: 4.31401
INFO:root:Validation iteration 40, Loss: 4.26360
INFO:root:Validation iteration 50, Loss: 4.21026
INFO:root:Validation iteration 60, Loss: 4.40243
INFO:root:Validation iteration 70, Loss: 4.23460
INFO:root:Validation iteration 80, Loss: 4.17919
INFO:root:Validation iteration 90, Loss: 4.10966
INFO:root:Validation iteration 100, Loss: 4.27734
INFO:root:Validation iteration 110, Loss: 4.47975
INFO:root:Validation iteration 120, Loss: 4.01939
INFO:root:Validation iteration 130, Loss: 4.17641
INFO:root:Validation iteration 140, Loss: 4.33517
INFO:root:Validation iteration 150, Loss: 4.25034
INFO:root:Validation iteration 160, Loss: 4.28731
INFO:root:Validation iteration 170, Loss: 4.21020
INFO:root:Validation iteration 180, Loss: 4.39564
INFO:root:Validation iteration 190, Loss: 4.19713
INFO:root:Validation iteration 200, Loss: 4.17740
INFO:root:Validation iteration 210, Loss: 4.20713
INFO:root:Validation iteration 220, Loss: 4.38755
INFO:root:Validation iteration 230, Loss: 4.43504
INFO:root:Validation iteration 240, Loss: 4.31480
INFO:root:Validation iteration 250, Loss: 4.36691
INFO:root:Validation iteration 260, Loss: 4.26459
INFO:root:End of Epoch 3
INFO:root:Training loss: 4.397
INFO:root:Validation accuracy: 0.055, Validation loss: 4.27175
INFO:root:Training epoch 4, Iteration 1, Loss: 4.29005
INFO:root:Training epoch 4, Iteration 30, Loss: 4.32977
INFO:root:Training epoch 4, Iteration 60, Loss: 4.33775
INFO:root:Training epoch 4, Iteration 90, Loss: 4.26188
INFO:root:Training epoch 4, Iteration 120, Loss: 4.38387
INFO:root:Training epoch 4, Iteration 150, Loss: 4.21704
INFO:root:Training epoch 4, Iteration 180, Loss: 4.23947
INFO:root:Training epoch 4, Iteration 210, Loss: 4.34572
INFO:root:Training epoch 4, Iteration 240, Loss: 4.27211
INFO:root:Training epoch 4, Iteration 270, Loss: 4.19903
INFO:root:Training epoch 4, Iteration 300, Loss: 4.34882
INFO:root:Training epoch 4, Iteration 330, Loss: 4.29131
INFO:root:Training epoch 4, Iteration 360, Loss: 4.24654
INFO:root:Training epoch 4, Iteration 390, Loss: 4.27180
INFO:root:Training epoch 4, Iteration 420, Loss: 4.20150
INFO:root:Training epoch 4, Iteration 450, Loss: 4.28569
INFO:root:Training epoch 4, Iteration 480, Loss: 4.15834
INFO:root:Training epoch 4, Iteration 510, Loss: 4.23883
INFO:root:Training epoch 4, Iteration 540, Loss: 4.24506
INFO:root:Training epoch 4, Iteration 570, Loss: 4.25676
INFO:root:Training epoch 4, Iteration 600, Loss: 4.21951
INFO:root:Training epoch 4, Iteration 630, Loss: 4.20011
INFO:root:Training epoch 4, Iteration 660, Loss: 4.08604
INFO:root:Training epoch 4, Iteration 690, Loss: 4.15573
INFO:root:Training epoch 4, Iteration 720, Loss: 4.19989
INFO:root:Training epoch 4, Iteration 750, Loss: 4.15650
INFO:root:Training epoch 4, Iteration 780, Loss: 4.22894
INFO:root:Validation iteration 1, Loss: 4.50620
INFO:root:Validation iteration 10, Loss: 4.15835
INFO:root:Validation iteration 20, Loss: 4.10688
INFO:root:Validation iteration 30, Loss: 4.13839
INFO:root:Validation iteration 40, Loss: 4.21339
INFO:root:Validation iteration 50, Loss: 4.13517
INFO:root:Validation iteration 60, Loss: 4.18847
INFO:root:Validation iteration 70, Loss: 4.16175
INFO:root:Validation iteration 80, Loss: 4.05121
INFO:root:Validation iteration 90, Loss: 3.87241
INFO:root:Validation iteration 100, Loss: 4.17626
INFO:root:Validation iteration 110, Loss: 4.34061
INFO:root:Validation iteration 120, Loss: 3.83381
INFO:root:Validation iteration 130, Loss: 4.12317
INFO:root:Validation iteration 140, Loss: 4.23145
INFO:root:Validation iteration 150, Loss: 4.16811
INFO:root:Validation iteration 160, Loss: 4.11964
INFO:root:Validation iteration 170, Loss: 4.02337
INFO:root:Validation iteration 180, Loss: 4.29539
INFO:root:Validation iteration 190, Loss: 4.03329
INFO:root:Validation iteration 200, Loss: 4.13664
INFO:root:Validation iteration 210, Loss: 4.03584
INFO:root:Validation iteration 220, Loss: 4.27103
INFO:root:Validation iteration 230, Loss: 4.33058
INFO:root:Validation iteration 240, Loss: 4.19112
INFO:root:Validation iteration 250, Loss: 4.23886
INFO:root:Validation iteration 260, Loss: 4.11457
INFO:root:End of Epoch 4
INFO:root:Training loss: 4.245
INFO:root:Validation accuracy: 0.068, Validation loss: 4.14657
INFO:root:Training epoch 5, Iteration 1, Loss: 3.98933
INFO:root:Training epoch 5, Iteration 30, Loss: 4.16129
INFO:root:Training epoch 5, Iteration 60, Loss: 4.16932
INFO:root:Training epoch 5, Iteration 90, Loss: 4.21567
INFO:root:Training epoch 5, Iteration 120, Loss: 4.18176
INFO:root:Training epoch 5, Iteration 150, Loss: 4.08870
INFO:root:Training epoch 5, Iteration 180, Loss: 4.07831
INFO:root:Training epoch 5, Iteration 210, Loss: 4.17181
INFO:root:Training epoch 5, Iteration 240, Loss: 4.07653
INFO:root:Training epoch 5, Iteration 270, Loss: 4.13300
INFO:root:Training epoch 5, Iteration 300, Loss: 4.24420
INFO:root:Training epoch 5, Iteration 330, Loss: 4.15217
INFO:root:Training epoch 5, Iteration 360, Loss: 4.17721
INFO:root:Training epoch 5, Iteration 390, Loss: 4.06469
INFO:root:Training epoch 5, Iteration 420, Loss: 4.18318
INFO:root:Training epoch 5, Iteration 450, Loss: 4.20340
INFO:root:Training epoch 5, Iteration 480, Loss: 4.12642
INFO:root:Training epoch 5, Iteration 510, Loss: 4.11811
INFO:root:Training epoch 5, Iteration 540, Loss: 4.05969
INFO:root:Training epoch 5, Iteration 570, Loss: 4.00848
INFO:root:Training epoch 5, Iteration 600, Loss: 4.07934
INFO:root:Training epoch 5, Iteration 630, Loss: 4.04984
INFO:root:Training epoch 5, Iteration 660, Loss: 4.02991
INFO:root:Training epoch 5, Iteration 690, Loss: 4.07194
INFO:root:Training epoch 5, Iteration 720, Loss: 4.07770
INFO:root:Training epoch 5, Iteration 750, Loss: 4.03862
INFO:root:Training epoch 5, Iteration 780, Loss: 4.07080
INFO:root:Validation iteration 1, Loss: 4.50268
INFO:root:Validation iteration 10, Loss: 4.10922
INFO:root:Validation iteration 20, Loss: 3.85971
INFO:root:Validation iteration 30, Loss: 4.02748
INFO:root:Validation iteration 40, Loss: 4.03980
INFO:root:Validation iteration 50, Loss: 4.05177
INFO:root:Validation iteration 60, Loss: 4.02673
INFO:root:Validation iteration 70, Loss: 3.97748
INFO:root:Validation iteration 80, Loss: 3.90401
INFO:root:Validation iteration 90, Loss: 3.78106
INFO:root:Validation iteration 100, Loss: 4.02789
INFO:root:Validation iteration 110, Loss: 4.16941
INFO:root:Validation iteration 120, Loss: 3.71029
INFO:root:Validation iteration 130, Loss: 3.90033
INFO:root:Validation iteration 140, Loss: 4.10067
INFO:root:Validation iteration 150, Loss: 4.02718
INFO:root:Validation iteration 160, Loss: 4.04514
INFO:root:Validation iteration 170, Loss: 3.88251
INFO:root:Validation iteration 180, Loss: 4.22744
INFO:root:Validation iteration 190, Loss: 3.97546
INFO:root:Validation iteration 200, Loss: 4.00086
INFO:root:Validation iteration 210, Loss: 3.81758
INFO:root:Validation iteration 220, Loss: 4.10799
INFO:root:Validation iteration 230, Loss: 4.14193
INFO:root:Validation iteration 240, Loss: 4.05449
INFO:root:Validation iteration 250, Loss: 4.13651
INFO:root:Validation iteration 260, Loss: 3.95196
INFO:root:End of Epoch 5
INFO:root:Training loss: 4.117
INFO:root:Validation accuracy: 0.082, Validation loss: 4.00522
INFO:root:Best validation accuracy: 0.082 at epoch 5
INFO:root:Inference...
INFO:root:Validation iteration 1, Loss: 3.50309
INFO:root:Validation iteration 10, Loss: 3.99725
INFO:root:Validation iteration 20, Loss: 4.08913
INFO:root:Validation iteration 30, Loss: 4.27031
INFO:root:Validation iteration 40, Loss: 4.00420
INFO:root:Validation iteration 50, Loss: 3.97209
INFO:root:Validation iteration 60, Loss: 3.84839
INFO:root:Validation iteration 70, Loss: 3.94016
INFO:root:Validation iteration 80, Loss: 4.21169
INFO:root:Validation iteration 90, Loss: 3.78485
INFO:root:Validation iteration 100, Loss: 3.99537
INFO:root:Validation iteration 110, Loss: 3.88057
INFO:root:Validation iteration 120, Loss: 3.87949
INFO:root:Validation iteration 130, Loss: 3.90611
INFO:root:Validation iteration 140, Loss: 3.98480
INFO:root:Validation iteration 150, Loss: 3.95736
INFO:root:Validation iteration 160, Loss: 3.94239
INFO:root:Validation iteration 170, Loss: 3.88051
INFO:root:Validation iteration 180, Loss: 4.03368
INFO:root:Validation iteration 190, Loss: 3.94115
INFO:root:Validation iteration 200, Loss: 3.93149
INFO:root:Validation iteration 210, Loss: 4.06357
INFO:root:Validation iteration 220, Loss: 4.13372
INFO:root:Validation iteration 230, Loss: 3.88759
INFO:root:Validation iteration 240, Loss: 4.00292
INFO:root:Validation iteration 250, Loss: 4.02727
INFO:root:Validation iteration 260, Loss: 3.97224
Test accuracy: 0.085, Test loss: 3.98996
INFO:root:Saving results...
INFO:root:Done!
"""

test = False
train_loss = []
val_loss = []
for line in string23.split("\n"):
    line = line.strip()
    
    if line.startswith("INFO:root:"):
        line = line[10:]
    else:
        continue
    
    print(line)
    try:
        if line.startswith("Training epoch"):
            train_loss.append(float(line.split(":")[1].strip()))
            
        if line.startswith("Validation iteration") and not test:
            val_loss.append(float(line.split(":")[1].strip()))
    except IndexError:
        pass
        
    if line.startswith("Inference..."):
        test = True
        
print(len(train_loss))
print(len(val_loss))
import matplotlib.pyplot as plt
import numpy as np

plt.plot(train_loss, label="Train")
#plt.plot(np.clip(val_loss, 0, 6), label="Validation")
#plt.ylim(0, max(max(train_loss), max(val_loss)) + 0.5)
plt.grid(which='both')
plt.legend()
plt.show()