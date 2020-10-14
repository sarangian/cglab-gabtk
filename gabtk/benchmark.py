#!/usr/bin/env python3
import luigi
import sys

from tasks.readCleaning.rawReadQC import readqc
from tasks.readCleaning.rawReadQC import rawReadsQC
from tasks.readCleaning.preProcessReads import cleanFastq
from tasks.readCleaning.preProcessReads import cleanReads
from tasks.readCleaning.preProcessReads import filtlong

from tasks.readCleaning.mecat2_correct import correctPAC
from tasks.readCleaning.necat_correct import correctONT

from tasks.assembly import skesa
from tasks.assembly import spades
from tasks.assembly import unicycler
from tasks.assembly import redundans
from tasks.assembly import lightassembler
from tasks.assembly import sparseassembler
from tasks.assembly import discovardenovo
from tasks.assembly import ray
from tasks.assembly import idba_ud
from tasks.assembly import abyss
from tasks.assembly import smartdenovo
from tasks.assembly import soapdenovo
from tasks.assembly import dbg2olc
from tasks.assembly import minia
from tasks.assembly import flye
from tasks.assembly import canu
from tasks.assembly import necat
from tasks.assembly import mecat2
from tasks.assembly import masurca
from tasks.assembly import abruijn
from tasks.assembly import wtdbg2
from tasks.assembly import miniasm
if __name__ == '__main__':

    luigi.run()
