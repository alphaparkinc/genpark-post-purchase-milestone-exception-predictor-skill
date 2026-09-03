from client import PostPurchaseMilestoneExceptionPredictorClient

def main():
    client = PostPurchaseMilestoneExceptionPredictorClient()
    res = client.predict_delivery_milestones('shp_01', 'UPS')
    print('Delivery Milestone Predictor: ' + res['milestone_id'])
    print('Predicted Delay: +' + str(res['predicted_delay_hours']) + ' hrs | ETA: ' + res['adjusted_eta_timestamp'])
    print('Milestone URL: ' + res['tracking_milestone_url'])

if __name__ == '__main__':
    main()
