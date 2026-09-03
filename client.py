class PostPurchaseMilestoneExceptionPredictorClient:
    def predict_delivery_milestones(self, shipment_id='shp_5519', carrier='FEDEX', current_status='WEATHER_DELAY_DENVER_HUB'):
        return {
            'milestone_id': 'mls_exc_5519',
            'shipment_id': shipment_id,
            'predicted_delay_hours': 24,
            'proactive_customer_notification_triggered': True,
            'adjusted_eta_timestamp': '2026-09-06T18:00:00Z',
            'apology_credit_granted_usd': 5.00,
            'tracking_milestone_url': 'https://narvar.tracking.genpark.ai/milestones/5519.json'
        }
