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

test = False
train_loss = []
val_loss = []
for line in string6.split("\n"):
    line = line.strip()
    
    if line.startswith("INFO:root:"):
        line = line[10:]
    else:
        continue
    
    print(line)
    try:
        if line.startswith("Training"):
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

plt.plot(train_loss, label="Train")
plt.plot(val_loss[-len(train_loss):], label="Validation")
plt.ylim(0, max(max(train_loss), max(val_loss)) + 0.5)
plt.legend()
plt.show()