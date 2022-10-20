class CoreAPI_Trainer:
    
    def __init__(self,
                 config=None,
                 algorithm=None,
                 core_context=None):
        self.config=config
        self.algorithm=algorithm
        self.core_context=core_context
        '''
        '''
        
    def restore_checkpoint(self):
        '''
        '''
        # self.algorithm.restore_checkpoint()
    
    def save_checkpoint(self):
        '''
        '''
        
    def fit(self):
        '''
        '''
        for op in self.core_context.searcher.operations():
            for epoch in range(next_epoch, op.length):
                # train for one epoch
                if args.rank == 0:
                    op.report_progress(epoch)
                
            next_epoch = op.length
            if args.rank == 0:
                op.report_completed(best_metric)
        
    
    def evaluate(self):
        '''
        '''
    
    def predict(self):
        