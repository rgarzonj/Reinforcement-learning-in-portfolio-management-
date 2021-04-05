import unittest
import json
from data.environment import Environment


class Test_Environment(unittest.TestCase):

    def setUp(self):
        self.env = Environment()

    #def tearDown(self):
        #self.widget.dispose()

    def test_create_environment(self):       
        
        self.assertNotEqual(self.env, None)

    def test_get_data(self):       
        with open('config.json') as f:
            config=json.load(f)
        start_date = config['session']['start_date']
        end_date = config['session']['end_date']
        codes_num = config['session']['codes']
        market = config['session']['market_types']
        features = config['session']['features']
        train_start_date, train_end_date, test_start_date, test_end_date, codes = self.env.get_repo(start_date, end_date,
                                                                                                   codes_num, market)
        window_length=10
        self.env.get_data(train_start_date, train_end_date, features, window_length, market, codes)    
        self.assertTrue(len(self.env.states)>0) # states has shape (1,6,10,2) 1,codes_num+1,window_length, features
        self.assertTrue(len(self.env.price_history)>0) #price_history has shape (6,1) codes_num + 1 ; 
        #First element in price_history is always 1, means cash
        #print (self.env.states[0].shape)
        #print (self.env.price_history[0].shape)
        #print (self.env.price_history[0])

    def test_get_repo(self):
        with open('config.json') as f:
            config=json.load(f)
        start_date = config['session']['start_date']
        end_date = config['session']['end_date']
        codes_num = config['session']['codes']
        market = config['session']['market_types']
        self.train_start_date, self.train_end_date, test_start_date, test_end_date, self.codes = self.env.get_repo(start_date, end_date,
                                                                                                   codes_num, market)
        self.assertTrue(len(self.env.data)>0)
        self.assertTrue(len(self.env.date_set)>0)

    # step requires get_data to have been called first to fill the environment.
    def test_step(self):
        self.test_get_data()
        self.env.reset()
        noise_flag = False
        info = self.env.step(None,None,noise_flag)
        # dict_keys(['reward', 'continue', 'next state', 'weight vector', 'price', 'risk'])
        #print (info.keys())
        #print (info['reward']) # Reward is an integer
        #print (info['continue']) # continue is True/False
        #print (info['next state'].shape) # Shape for next state is (1,6,10,2)
        #print (info['weight vector'].shape) # Shape for weight vector is (1,6)
        #print (info['risk']) #Risk is an integer
        #print (info['price'].shape) #Shape for price is 6,1)
        self.assertEqual(len(info.keys(),6))


if __name__ == '__main__':
    unittest.main()