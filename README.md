# Reinforcement learning in portfolio management

## Introduction

Motivated by "A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem" by [Jiang et. al. 2017](https://arxiv.org/abs/1706.10059) [1]. In this project:
+ Implement two state-of-art continuous deep reinforcement learning algorithms, Deep Deterministic Policy Gradient (DDPG), Proximal Policy Optimization (PPO) and compared them with PG in Finance purposed by Jiang et. al. in portfolio management. 
+ Experiments on different settings, such as changing learning rates, optimizers, neutral network structures, China/America Stock data, initializers, noise, features to figure out their influence on the RL agents' performance (cumulative return).

## Using the environment

The environment provides supports for easily testing different reinforcement learning in portfolio management.
+ main.py -  the entrance to run our training and testing framework
+ ./result- contains subfolders named by number, involving the settings and result in a particular experiment.
+ ./summary- contains summaries, also with DDPG, PPO and PG sub folder
+ ./agent- contains ddpg.py, ppo.py and ornstein_uhlenbeck.py(the noise we add to agent's actions during training)
+ ./data- contains America.csv for USA stock data, China.csv for China stock data. download_data.py can download China stock data by Tushare. environment.py generates states data for trading agents.
+ config.json- the configuration file for training or testing settings:
```
{
	"data":{
		"start_date":"2015-01-01",
		"end_date":"2018-01-01",
		"market_types":["stock"],
		"ktype":"D"
	},
	"session":{
		"start_date":"2007-01-01",
		"end_date":"2018-12-30",
		"market_types":"China",
	    "codes":5,
		"features":["close","high"],
		"agents":["CNN","PG","10"],
		"epochs":"100",
		"noise_flag":"False",
		"record_flag":"False",
		"plot_flag":"False",
		"reload_flag":"False",
		"trainable":"True",
		"method":"model_free"
	}
}
```

Download stock data in Shenzhen and Shanghai stock market in the given period in Day(D) frequency. Options: hours, minutes (Not recommended in this version. We provide higher quality data in folder data)
```
python main.py --mode=download_data
```
Training/Testing
```
python main.py --mode=train --num=1
```
**The program will randomly select a fixed number of assets from the data, ensuring the intersection of their valid time exceeds the threshold set in json in order to guarantee enough information for training. All the saved network and summary will be store in a specified subfolder in ./result**

```
python main.py --mode=test --num=1
```
Backtest the network in subfolder named 1

+ noise_flag=True: actions produced by RL agents are distorted by adding UO noise.
+ record_flag=True: trading details would be stored as a csv file named by the epoch and cumulative return each epoch.
+ plot_flag=True: the trend of wealth would be plot each epoch.
+ reload_flag=True: tensorflow would search latest saved model in ./saved_network and reload.
+ trainable=True: parameters would be updated during each epoch.
+ method=model_based: the first epochs our agents would try to imitate a greedy strategy to quickly improve its performance. Then it would leave it and continue to self-improve by model-free reinforcement learning.

## Result
+ Training data (USA)_DDPG
  ![USA](image/USA.png)
+ Training data (China)_DDPG
  ![China](image/China.png)

+ Backtest (USA)_DDPG
  ![backtest_USA](image/backtest_USA.png)

+ Backtest (China)_PG
  ![result1](image/result1.png)

+ APV under different feature combinations
  ![features_reward](image/features_reward.png)

**The other results can be found in our report:** [**English Version**](https://arxiv.org/abs/1808.09940) and [**Chinese Version**](https://github.com/qq303067814/Reinforcement-learning-in-portfolio-management-/blob/master/report/%E6%B7%B1%E5%BA%A6%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0%E5%9C%A8%E8%B5%84%E4%BA%A7%E9%85%8D%E7%BD%AE%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8.pdf).

COnclusions: PG can achieve best performance both in training and backtest against DDPG and PPO. 
**We also notice that adding noise in prices data can significantly improve the performance in training and backtest, which can somehow be explained in robust MDP way.**




## Contribution

### Contributors

* ***Zhipeng Liang***
* ***Kangkang Jiang***
* ***Hao Chen***
* ***Junhao Zhu***
* ***Yanran Li***
### Institutions

+ ***AI&FintechLab of Likelihood Technology***
+ ***Sun Yat-sen University***

## Acknowledegment

We would like to say thanks to ***Mingwen Liu*** from ***ShingingMidas Private Fund***, ***Zheng Xie*** and ***Xingyu Fu*** from ***Sun Yat-sen University*** for their generous guidance throughout the project.

## Set up

Python Version

+ ***3.6***

Modules needed

+ ***tensorflow(tensorflow-gpu)***
+ ***numpy*** 
+ ***pandas*** 
+ ***matplotlib***

## Contact

+ liangzhp6@mail2.sysu.edu.cn
+ jiangkk3@mail2.sysu.edu.cn
+ chenhao348@mail2.sysu.edu.cn
+ zhujh25@mail2.sysu.edu.cn
+ liyr8@mail2.sysu.edu.cn
