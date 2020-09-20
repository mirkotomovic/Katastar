CREATE TABLE IF NOT EXISTS `nepokretnost` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `RefBr` VARCHAR(120) NULL,
    `matBrOpstine` INT(6) NULL,
    `nazivOpstine` VARCHAR(120) NULL,
    `matBrKatOpstine` INT(7) NULL,
    `nazivKatOpstine` VARCHAR(120) NULL,
    `datumAzuriranja` VARCHAR(120) NULL,
    `sluzba` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `alist` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `Ulica` VARCHAR(120) NULL,
    `brParcele` INt(6) NULL,
    `podBrParcele` INT(7) NULL,
    `površina` VARCHAR(120) NULL,
    `brListaNepokretnosti` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `deoParcele` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    
    `brDela` INT(10) NULL,
    `vrstaZemljista` VARCHAR(120) NULL,
    `kultura` VARCHAR(120) NULL,
    `povrsinaDela` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `B1List` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,

    `brObjekta` INT(7) NULL,
    `nazivUlice` VARCHAR(120) NULL,
    `brKuce` VARCHAR(120) NULL,
    `podBrKuce` VARCHAR(120) NULL,
    `povrsinaB1` VARCHAR(120) NULL,
    `korisnaPovrsina` VARCHAR(120) NULL,
    `gradjPovrsina` VARCHAR(120) NULL,
    `nacinKoriscenja` VARCHAR(120) NULL,
    `pravniStatus` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `B2List` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,

    `brObjekta_B2List` VARCHAR(120) NULL,
    `nazivUlice_B2List` VARCHAR(120) NULL,
    `brUlaza_B2List` VARCHAR(120) NULL,
    `brEvid_B2List` VARCHAR(120) NULL,
    `nacinKoriscenja_B2List` VARCHAR(120) NULL,
    `brPosebnogDela_B2List` VARCHAR(120) NULL,
    `podBrPosebnogDela_B2List` VARCHAR(120) NULL,
    `gradjPovrsinaB2_B2List` VARCHAR(120) NULL,
    `korisnaPovrsinaB2_B2List` VARCHAR(120) NULL,
    `nacinUtvridjivanjaKorisnePovrsine_B2List` VARCHAR(120) NULL,
    `opis_B2List` TEXT NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `imaociParcele` (
    `idImaociParcele` int(11) NOT NULL AUTO_INCREMENT,

    `naziv` VARCHAR(120) NULL,
    `vrstaPrava` VARCHAR(120) NULL,
    `oplikSvojine` VARCHAR(120) NULL,
    `udeo` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idImaociParcele`)
);

CREATE TABLE IF NOT EXISTS `teretParcele` (
    `idTeretParcele` int(11) NOT NULL AUTO_INCREMENT,

    `brTereta` VARCHAR(120) NULL,
    `vrstaTereta` VARCHAR(120) NULL,
    `datumUpisa` VARCHAR(120) NULL,
    `trajanjeTereta` VARCHAR(120) NULL,
    `datumPrestanka` VARCHAR(120) NULL,
    `opisTereta` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idTeretParcele`)
);

CREATE TABLE IF NOT EXISTS `zabelezbaParcele` (
    `idZabelezbaParcele` int(11) NOT NULL AUTO_INCREMENT,

    `datum` VARCHAR(120) NULL,
    `brPredmeta` VARCHAR(120) NULL,
    `opis` TEXT NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idZabelezbaParcele`)
);

CREATE TABLE IF NOT EXISTS `imaociObjekta` (
    `idImaociPodObjekta` int(11) NOT NULL AUTO_INCREMENT,

    `naziv` VARCHAR(120) NULL,
    `vrstaPrava` VARCHAR(120) NULL,
    `oplikSvojine` VARCHAR(120) NULL,
    `udeo` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idImaociPodObjekta`)
);

CREATE TABLE IF NOT EXISTS `teretObjekta` (
    `idTeretObjekta` int(11) NOT NULL AUTO_INCREMENT,

    `brTereta` VARCHAR(120) NULL,
    `vrstaTereta` VARCHAR(120) NULL,
    `datumUpisa` VARCHAR(120) NULL,
    `trajanjeTereta` VARCHAR(120) NULL,
    `datumPrestanka` VARCHAR(120) NULL,
    `opisTereta` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idTeretObjekta`)
);

CREATE TABLE IF NOT EXISTS `zabelezbaObjekta` (
    `idZabelezbaObjekta` int(11) NOT NULL AUTO_INCREMENT,
    
    `datum` VARCHAR(120) NULL,
    `brPredmeta` VARCHAR(120) NULL,
    `opis` TEXT NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idZabelezbaObjekta`)
);

CREATE TABLE IF NOT EXISTS `imaociPodObjekta` (
    `idImaociPodObjekta` int(11) NOT NULL AUTO_INCREMENT,

    `naziv` VARCHAR(120) NULL,
    `vrstaPrava` VARCHAR(120) NULL,
    `oplikSvojine` VARCHAR(120) NULL,
    `udeo` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idImaociPodObjekta`)
);

CREATE TABLE IF NOT EXISTS `teretPodObjekta` (
    `idTeretPodObjekta` int(11) NOT NULL AUTO_INCREMENT,

    `brTereta` VARCHAR(120) NULL,
    `vrstaTereta` VARCHAR(120) NULL,
    `datumUpisa` VARCHAR(120) NULL,
    `trajanjeTereta` VARCHAR(120) NULL,
    `datumPrestanka` VARCHAR(120) NULL,
    `opisTereta` VARCHAR(120) NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idTeretPodObjekta`)
);

CREATE TABLE IF NOT EXISTS `zabelezbaPodObjekta` (
    `idZabelezbaPodObjekta` int(11) NOT NULL AUTO_INCREMENT,

    `datum` VARCHAR(120) NULL,
    `brPredmeta` VARCHAR(120) NULL,
    `opis` TEXT NULL,

    `id_lista` VARCHAR(120) NULL,
    PRIMARY KEY (`idZabelezbaPodObjekta`)
);
