from CMGTools.RootTools.fwlite.Analyzer import Analyzer
from CMGTools.RootTools.fwlite.Event import Event
from CMGTools.RootTools.statistics.Counter import Counter, Counters
from CMGTools.RootTools.fwlite.AutoHandle import AutoHandle

class ttHGenSkimmer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(ttHGenSkimmer,self).__init__(cfg_ana,cfg_comp,looperName)

    def declareHandles(self):
        super(ttHGenSkimmer, self).declareHandles()

    def beginLoop(self):
        super(ttHGenSkimmer,self).beginLoop()
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('pass gen Zmumu skim')
        count.register('pass gen ttbar 1L skim')
        count.register('accepted events')


    def process(self, iEvent, event):
        self.readCollections( iEvent )
        self.counters.counter('events').inc('all events')

        if len(genleps)==1 and len(gentaus)==1:
            self.counters.counter('events').inc('pass gen ttbar 1L skim')

        if len(genleps)==2:
            if jets[0].pdgId()==13 and jets[1].pdgId()==13 and jets[0].sourceId()==23 and jets[1].sourceId()==23:
                self.counters.counter('events').inc('pass gen Zmumu skim')

        self.counters.counter('events').inc('accepted events')
        return True
