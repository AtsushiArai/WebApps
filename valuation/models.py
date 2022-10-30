from time import timezone
from django.db import models

# Create your models here.
class FinancialData(models.Model):
    __tablename__ = 'financial_data'
    # id = models.IntegerField(primary_key=True)
    uid = models.CharField(max_length=300, primary_key=True)
    year_before_last = models.CharField(max_length=10)
    last_year = models.CharField(max_length=10)
    this_year = models.CharField(max_length=10)
    
    ############### year_before_last : t - 2 ####################
    ybl_net_sales = models.IntegerField(default=0)
    ybl_cogs = models.IntegerField(default=0)
    # ybl_gross_profit = models.IntegerField(default=0)
    ybl_sga = models.IntegerField(default=0)
    ybl_operating_income = models.IntegerField(default=0)
    
    ybl_interest_and_dividends_income = models.IntegerField(default=0)
    ybl_equity_in_earnings_or_losses_of_affiliates = models.IntegerField(default=0)
    # ybl_other_non_operating_income = models.IntegerField(default=0)
    # ybl_non_operating_income = models.IntegerField(default=0)

    ybl_interest_expenses = models.IntegerField(default=0)
    # ybl_equity_in_losses_of_affiliates = models.IntegerField(default=0)
    # ybl_other_non_operating_expenses = models.IntegerField(default=0)
    # ybl_non_operating_expenses = models.IntegerField(default=0)
    ybl_ordinary_income_loss = models.IntegerField(default=0)
    ybl_other_nonoperating_income_or_loss = models.IntegerField(default=0)

    ybl_extraordinary_income_and_loss = models.IntegerField(default=0)
    ybl_income_before_income_taxes = models.IntegerField(default=0)
    ybl_income_taxes = models.IntegerField(default=0)
    ybl_profit_loss_attributable_to_non_controling_interests = models.IntegerField(default=0)
    ybl_profit_loss_attributable_to_owners_of_parent = models.IntegerField(default=0)

    ybl_depreciation = models.IntegerField(default=0)
    ybl_amortization_goodwill = models.IntegerField(default=0)
    ybl_impairment = models.IntegerField(default=0)

    ################  BS  ######################
    ybl_cash_and_deposits = models.IntegerField(default=0)
    ybl_securities = models.IntegerField(default=0)
    ybl_notes_and_accounts_receivable_trade = models.IntegerField(default=0)
    ybl_inventories = models.IntegerField(default=0)
    ybl_deferred_tax_assets_ca = models.IntegerField(default=0)
    ybl_other_current_assets = models.IntegerField(default=0)
    ybl_current_assets = models.IntegerField(default=0)

    ybl_property_plant_and_equipment = models.IntegerField(default=0)
    
    ybl_intangible_assets = models.IntegerField(default=0)

    ybl_deferred_tax_assets_ioa = models.IntegerField(default=0)
    ybl_investments_and_other_assets = models.IntegerField(default=0)
    
    ybl_total_assets = models.IntegerField(default=0)

    ybl_short_term_interest_bearing_bond = models.IntegerField(default=0)
    ybl_notes_and_accounts_payable_trade = models.IntegerField(default=0)
    ybl_deferred_tax_liabilities_ca = models.IntegerField(default=0)
    ybl_other_current_liabilities = models.IntegerField(default=0)
    ybl_current_liabilities = models.IntegerField(default=0)

    ybl_long_term_interest_bearing_bond = models.IntegerField(default=0)
    ybl_deferred_tax_liabilities_ncl = models.IntegerField(default=0)
    ybl_other_noncurrent_liabilities = models.IntegerField(default=0)
    ybl_noncurrent_liabilities = models.IntegerField(default=0)

    ybl_capital_stock = models.IntegerField(default=0)
    ybl_capital_surplus = models.IntegerField(default=0)
    ybl_retained_earnings = models.IntegerField(default=0)
    ybl_treasury_stock = models.IntegerField(default=0)
    ybl_accumulated_other_comprehensive_income = models.IntegerField(default=0)
    ybl_subscription_rights_to_shares = models.IntegerField(default=0)
    ybl_non_controlling_interests = models.IntegerField(default=0)
    ybl_net_assets = models.IntegerField(default=0)

    ybl_liabilities_and_net_assets = models.IntegerField(default=0)
    ybl_net_deferred_tax_assets = models.IntegerField(default=0)

    ################  SS  ######################
    ybl_net_assets_py = models.IntegerField(default=0)
    ybl_issuance_of_new_shares = models.IntegerField(default=0)
    ybl_dividends_ss = models.IntegerField(default=0)
    ybl_purchase_of_treasury_stock = models.IntegerField(default=0)
    ybl_disposal_of_treasury_stock = models.IntegerField(default=0)

    ################  CF  ######################
    # ybl_cf_operating_activities = models.IntegerField(default=0)
    # ybl_cf_investment_activities = models.IntegerField(default=0)
    # ybl_cf_financing_activities = models.IntegerField(default=0)

    ################ OHTER ####################
    ybl_total_number_of_issued_shares = models.IntegerField(default=0)
    ybl_number_of_shares_held_in_own_name = models.IntegerField(default=0)
    ybl_dividend_paid_per_share = models.IntegerField(default=0)
    ybl_effective_tax_rate = models.FloatField(default=0.0)

    ############### INVESTED_CAPITAL #####################
    ybl_invested_capital = models.FloatField(default=0.0)

    ############### last_year : t - 1 ###########################
    ly_net_sales = models.IntegerField(default=0)
    ly_cogs = models.IntegerField(default=0)
    # ly_gross_profit = models.IntegerField(default=0)
    ly_sga = models.IntegerField(default=0)
    ly_operating_income = models.IntegerField(default=0)
    
    ly_interest_and_dividends_income = models.IntegerField(default=0)
    ly_equity_in_earnings_or_losses_of_affiliates = models.IntegerField(default=0)
    # ly_other_non_operating_income = models.IntegerField(default=0)
    # ly_non_operating_income = models.IntegerField(default=0)

    ly_interest_expenses = models.IntegerField(default=0)
    # ly_equity_in_losses_of_affiliates = models.IntegerField(default=0)
    # ly_other_non_operating_expenses = models.IntegerField(default=0)
    # ly_non_operating_expenses = models.IntegerField(default=0)
    ly_ordinary_income_loss = models.IntegerField(default=0)
    ly_other_nonoperating_income_or_loss = models.IntegerField(default=0)

    ly_extraordinary_income_and_loss = models.IntegerField(default=0)
    ly_income_before_income_taxes = models.IntegerField(default=0)
    ly_income_taxes = models.IntegerField(default=0)
    ly_profit_loss_attributable_to_non_controling_interests = models.IntegerField(default=0)
    ly_profit_loss_attributable_to_owners_of_parent = models.IntegerField(default=0)

    ly_depreciation = models.IntegerField(default=0)
    ly_amortization_goodwill = models.IntegerField(default=0)
    ly_impairment = models.IntegerField(default=0)

    ################  BS  ######################
    ly_cash_and_deposits = models.IntegerField(default=0)
    ly_securities = models.IntegerField(default=0)
    ly_notes_and_accounts_receivable_trade = models.IntegerField(default=0)
    ly_inventories = models.IntegerField(default=0)
    ly_deferred_tax_assets_ca = models.IntegerField(default=0)
    ly_other_current_assets = models.IntegerField(default=0)
    ly_current_assets = models.IntegerField(default=0)

    ly_property_plant_and_equipment = models.IntegerField(default=0)
    
    ly_intangible_assets = models.IntegerField(default=0)

    ly_deferred_tax_assets_ioa = models.IntegerField(default=0)
    ly_investments_and_other_assets = models.IntegerField(default=0)
    
    ly_total_assets = models.IntegerField(default=0)

    ly_short_term_interest_bearing_bond = models.IntegerField(default=0)
    ly_notes_and_accounts_payable_trade = models.IntegerField(default=0)
    ly_deferred_tax_liabilities_ca = models.IntegerField(default=0)
    ly_other_current_liabilities = models.IntegerField(default=0)
    ly_current_liabilities = models.IntegerField(default=0)

    ly_long_term_interest_bearing_bond = models.IntegerField(default=0)
    ly_deferred_tax_liabilities_ncl = models.IntegerField(default=0)
    ly_other_noncurrent_liabilities = models.IntegerField(default=0)
    ly_noncurrent_liabilities = models.IntegerField(default=0)

    ly_capital_stock = models.IntegerField(default=0)
    ly_capital_surplus = models.IntegerField(default=0)
    ly_retained_earnings = models.IntegerField(default=0)
    ly_treasury_stock = models.IntegerField(default=0)
    ly_accumulated_other_comprehensive_income = models.IntegerField(default=0)
    ly_subscription_rights_to_shares = models.IntegerField(default=0)
    ly_non_controlling_interests = models.IntegerField(default=0)
    ly_net_assets = models.IntegerField(default=0)

    ly_liabilities_and_net_assets = models.IntegerField(default=0)
    ly_net_deferred_tax_assets = models.IntegerField(default=0)
    ly_fluctuations_in_deferred_tax_assets = models.IntegerField(default=0)

    ################  SS  ######################
    ly_net_assets_py = models.IntegerField(default=0)
    ly_issuance_of_new_shares = models.IntegerField(default=0)
    ly_dividends_ss = models.IntegerField(default=0)
    ly_purchase_of_treasury_stock = models.IntegerField(default=0)
    ly_disposal_of_treasury_stock = models.IntegerField(default=0)

    ################  CF  ######################
    # ly_cf_operating_activities = models.IntegerField(default=0)
    # ly_cf_investment_activities = models.IntegerField(default=0)
    # ly_cf_financing_activities = models.IntegerField(default=0)

    ################ OHTER ####################
    ly_total_number_of_issued_shares = models.IntegerField(default=0)
    ly_number_of_shares_held_in_own_name = models.IntegerField(default=0)
    ly_dividend_paid_per_share = models.IntegerField(default=0)
    ly_effective_tax_rate = models.FloatField(default=0.0)

    ################ TAX_ON_OPERATING_INCOME ####################
    ly_tax_on_interest_income_and_dividend = models.IntegerField(default=0)
    ly_tax_on_interest_expenses = models.IntegerField(default=0)
    ly_tax_on_non_operating_income_and_expenses_others = models.IntegerField(default=0)
    ly_tax_on_extraordinary_income_and_losses = models.IntegerField(default=0)
    ly_tax_on_operating_income = models.IntegerField(default=0)

    ############### NOPAT_TOPDOWN #####################
    ly_nopat_topdown = models.IntegerField(default=0)

    ############### NOPAT_BOTTOMUP #####################
    ly_nopat_bottomup = models.IntegerField(default=0)

    ############### INVESTMENT_CAPITAL #####################
    ly_net_working_capital = models.IntegerField(default=0)
    ly_investment_capital = models.IntegerField(default=0)

    ############### FREE_CASH_FLOW #####################
    ly_operating_cf = models.IntegerField(default=0)
    ly_investment_cf = models.IntegerField(default=0)
    ly_free_cash_flow = models.IntegerField(default=0)
    ly_non_operating_cf = models.IntegerField(default=0)
    ly_financial_cf = models.IntegerField(default=0)
    ly_net_cf = models.IntegerField(default=0)

    ############### ROE #####################
    ly_return_on_equity = models.FloatField(default=0)
    ly_return_on_asset = models.FloatField(default=0)
    ly_total_asset_turnover = models.FloatField(default=0)
    ly_financial_leverage = models.FloatField(default=0)

    ############### WACC #####################


    ############### ROIC #####################
    ly_return_on_invested_capital = models.FloatField(default=0)
    ly_return_on_invested_capital_before_tax = models.FloatField(default=0)
    ly_tax_burden_rate = models.FloatField(default=0)
    ly_affiliated_company_contribution_rate = models.FloatField(default=0)
    ly_operating_profit_margin = models.FloatField(default=0)
    ly_cost_rate = models.FloatField(default=0)
    ly_sga_ratio = models.FloatField(default=0)
    ly_invested_capital_turnover = models.FloatField(default=0)
    ly_net_working_capital_turnover_days = models.FloatField(default=0)
    ly_trade_receivavle_turnover_days = models.FloatField(default=0)
    ly_trade_payable_turnover_days = models.FloatField(default=0)
    ly_inventries_turnover_days = models.FloatField(default=0)
    ly_property_turnover_days = models.FloatField(default=0)
    ly_intangible_turnover_days = models.FloatField(default=0)
    ly_other_invested_capital_turnover_days = models.FloatField(default=0)
    ly_cash_conversion_cicle = models.FloatField(default=0)


    ############### this_year : t ###############################
    net_sales = models.IntegerField(default=0)
    cogs = models.IntegerField(default=0)
    # gross_profit = models.IntegerField(default=0)
    sga = models.IntegerField(default=0)
    operating_income = models.IntegerField(default=0)
    
    interest_and_dividends_income = models.IntegerField(default=0)
    equity_in_earnings_or_losses_of_affiliates = models.IntegerField(default=0)
    # other_non_operating_income = models.IntegerField(default=0)
    # non_operating_income = models.IntegerField(default=0)

    interest_expenses = models.IntegerField(default=0)
    # equity_in_losses_of_affiliates = models.IntegerField(default=0)
    # other_non_operating_expenses = models.IntegerField(default=0)
    # non_operating_expenses = models.IntegerField(default=0)
    ordinary_income_loss = models.IntegerField(default=0)
    other_nonoperating_income_or_loss = models.IntegerField(default=0)

    extraordinary_income_and_loss = models.IntegerField(default=0)
    income_before_income_taxes = models.IntegerField(default=0)
    income_taxes = models.IntegerField(default=0)
    profit_loss_attributable_to_non_controling_interests = models.IntegerField(default=0)
    profit_loss_attributable_to_owners_of_parent = models.IntegerField(default=0)

    depreciation = models.IntegerField(default=0)
    amortization_goodwill = models.IntegerField(default=0)
    impairment = models.IntegerField(default=0)

    ################  BS  ######################
    cash_and_deposits = models.IntegerField(default=0)
    securities = models.IntegerField(default=0)
    notes_and_accounts_receivable_trade = models.IntegerField(default=0)
    inventories = models.IntegerField(default=0)
    deferred_tax_assets_ca = models.IntegerField(default=0)
    other_current_assets = models.IntegerField(default=0)
    current_assets = models.IntegerField(default=0)

    property_plant_and_equipment = models.IntegerField(default=0)
    
    intangible_assets = models.IntegerField(default=0)

    deferred_tax_assets_ioa = models.IntegerField(default=0)
    investments_and_other_assets = models.IntegerField(default=0)
    
    total_assets = models.IntegerField(default=0)

    short_term_interest_bearing_bond = models.IntegerField(default=0)
    notes_and_accounts_payable_trade = models.IntegerField(default=0)
    deferred_tax_liabilities_ca = models.IntegerField(default=0)
    other_current_liabilities = models.IntegerField(default=0)
    current_liabilities = models.IntegerField(default=0)

    long_term_interest_bearing_bond = models.IntegerField(default=0)
    deferred_tax_liabilities_ncl = models.IntegerField(default=0)
    other_noncurrent_liabilities = models.IntegerField(default=0)
    noncurrent_liabilities = models.IntegerField(default=0)

    capital_stock = models.IntegerField(default=0)
    capital_surplus = models.IntegerField(default=0)
    retained_earnings = models.IntegerField(default=0)
    treasury_stock = models.IntegerField(default=0)
    accumulated_other_comprehensive_income = models.IntegerField(default=0)
    subscription_rights_to_shares = models.IntegerField(default=0)
    non_controlling_interests = models.IntegerField(default=0)
    net_assets = models.IntegerField(default=0)

    liabilities_and_net_assets = models.IntegerField(default=0)
    net_deferred_tax_assets = models.IntegerField(default=0)
    fluctuations_in_deferred_tax_assets = models.IntegerField(default=0)

    ################  SS  ######################
    net_assets_py = models.IntegerField(default=0)
    issuance_of_new_shares = models.IntegerField(default=0)
    dividends_ss = models.IntegerField(default=0)
    purchase_of_treasury_stock = models.IntegerField(default=0)
    disposal_of_treasury_stock = models.IntegerField(default=0)

    ################  CF  ######################
    # cf_operating_activities = models.IntegerField(default=0)
    # cf_investment_activities = models.IntegerField(default=0)
    # cf_financing_activities = models.IntegerField(default=0)

    ################ OHTER ####################
    total_number_of_issued_shares = models.IntegerField(default=0)
    number_of_shares_held_in_own_name = models.IntegerField(default=0)
    dividend_paid_per_share = models.IntegerField(default=0)
    effective_tax_rate = models.FloatField(default=0.0)

    ################ TAX_ON_OPERATING_INCOME ####################
    tax_on_interest_income_and_dividend = models.IntegerField(default=0)
    tax_on_interest_expenses = models.IntegerField(default=0)
    tax_on_non_operating_income_and_expenses_others = models.IntegerField(default=0)
    tax_on_extraordinary_income_and_losses = models.IntegerField(default=0)
    tax_on_operating_income = models.IntegerField(default=0)

    ############### NOPAT_TOPDOWN #####################
    nopat_topdown = models.IntegerField(default=0)

    ############### NOPAT_BOTTOMUP #####################
    nopat_bottomup = models.IntegerField(default=0)

    ############### INVESTED_CAPITAL #####################
    net_working_capital = models.IntegerField(default=0)
    investment_capital = models.IntegerField(default=0)

    ############### FREE_CASH_FLOW #####################
    operating_cf = models.IntegerField(default=0)
    investment_cf = models.IntegerField(default=0)
    free_cash_flow = models.IntegerField(default=0)
    non_operating_cf = models.IntegerField(default=0)
    financial_cf = models.IntegerField(default=0)
    net_cf = models.IntegerField(default=0)

    ############### ROE #####################
    return_on_equity = models.FloatField(default=0)
    return_on_asset = models.FloatField(default=0)
    total_asset_turnover = models.FloatField(default=0)
    financial_leverage = models.FloatField(default=0)

    ############### WACC #####################
    borrowing_interest_rate = models.FloatField(default=0)
    risk_free_rate = models.FloatField(default=0)
    cost_of_shareholders_equity = models.FloatField(default=0)
    wacc = models.FloatField(default=0)

    ############### ROIC #####################
    return_on_invested_capital = models.FloatField(default=0)
    return_on_invested_capital_before_tax = models.FloatField(default=0)
    tax_burden_rate = models.FloatField(default=0)
    affiliated_company_contribution_rate = models.FloatField(default=0)
    operating_profit_margin = models.FloatField(default=0)
    cost_rate = models.FloatField(default=0)
    sga_ratio = models.FloatField(default=0)
    invested_capital_turnover = models.FloatField(default=0)
    net_working_capital_turnover_days = models.FloatField(default=0)
    trade_receivavle_turnover_days = models.FloatField(default=0)
    trade_payable_turnover_days = models.FloatField(default=0)
    inventries_turnover_days = models.FloatField(default=0)
    property_turnover_days = models.FloatField(default=0)
    intangible_turnover_days = models.FloatField(default=0)
    other_invested_capital_turnover_days = models.FloatField(default=0)
    cash_conversion_cicle = models.FloatField(default=0)

    valuation_01 = models.IntegerField(default=0)
    wacc_adj_01 = models.FloatField(default=0)
    grows_rate_01 = models.FloatField(default=0)
    valuation_02 = models.IntegerField(default=0)
    wacc_adj_02 = models.FloatField(default=0)
    grows_rate_02 = models.FloatField(default=0)
    valuation_03 = models.IntegerField(default=0)
    wacc_adj_03 = models.FloatField(default=0)
    grows_rate_03 = models.FloatField(default=0)
    valuation_04 = models.IntegerField(default=0)
    wacc_adj_04 = models.FloatField(default=0)
    grows_rate_04 = models.FloatField(default=0)
    valuation_05 = models.IntegerField(default=0)
    wacc_adj_05 = models.FloatField(default=0)
    grows_rate_05 = models.FloatField(default=0)
    valuation_06 = models.IntegerField(default=0)
    wacc_adj_06 = models.FloatField(default=0)
    grows_rate_06 = models.FloatField(default=0)
    valuation_07 = models.IntegerField(default=0)
    wacc_adj_07 = models.FloatField(default=0)
    grows_rate_07 = models.FloatField(default=0)
    valuation_08 = models.IntegerField(default=0)
    wacc_adj_08 = models.FloatField(default=0)
    grows_rate_08 = models.FloatField(default=0)
    valuation_09 = models.IntegerField(default=0)
    wacc_adj_09 = models.FloatField(default=0)
    grows_rate_09 = models.FloatField(default=0)
    valuation_10 = models.IntegerField(default=0)
    wacc_adj_10 = models.FloatField(default=0)
    grows_rate_10 = models.FloatField(default=0)
    valuation_11 = models.IntegerField(default=0)
    wacc_adj_11 = models.FloatField(default=0)
    grows_rate_11 = models.FloatField(default=0)
    valuation_12 = models.IntegerField(default=0)
    wacc_adj_12 = models.FloatField(default=0)
    grows_rate_12 = models.FloatField(default=0)
    valuation_13 = models.IntegerField(default=0)
    wacc_adj_13 = models.FloatField(default=0)
    grows_rate_13 = models.FloatField(default=0)
    valuation_14 = models.IntegerField(default=0)
    wacc_adj_14 = models.FloatField(default=0)
    grows_rate_14 = models.FloatField(default=0)
    valuation_15 = models.IntegerField(default=0)
    wacc_adj_15 = models.FloatField(default=0)
    grows_rate_15 = models.FloatField(default=0)
    valuation_16 = models.IntegerField(default=0)
    wacc_adj_16 = models.FloatField(default=0)
    grows_rate_16 = models.FloatField(default=0)
    valuation_17 = models.IntegerField(default=0)
    wacc_adj_17 = models.FloatField(default=0)
    grows_rate_17 = models.FloatField(default=0)
    valuation_18 = models.IntegerField(default=0)
    wacc_adj_18 = models.FloatField(default=0)
    grows_rate_18 = models.FloatField(default=0)
    valuation_19 = models.IntegerField(default=0)
    wacc_adj_19 = models.FloatField(default=0)
    grows_rate_19 = models.FloatField(default=0)
    valuation_20 = models.IntegerField(default=0)
    wacc_adj_20 = models.FloatField(default=0)
    grows_rate_20 = models.FloatField(default=0)
    valuation_21 = models.IntegerField(default=0)
    wacc_adj_21 = models.FloatField(default=0)
    grows_rate_21 = models.FloatField(default=0)
    valuation_22 = models.IntegerField(default=0)
    wacc_adj_22 = models.FloatField(default=0)
    grows_rate_22 = models.FloatField(default=0)
    valuation_23 = models.IntegerField(default=0)
    wacc_adj_23 = models.FloatField(default=0)
    grows_rate_23 = models.FloatField(default=0)
    valuation_24 = models.IntegerField(default=0)
    wacc_adj_24 = models.FloatField(default=0)
    grows_rate_24 = models.FloatField(default=0)
    valuation_25 = models.IntegerField(default=0)
    wacc_adj_25 = models.FloatField(default=0)
    grows_rate_25 = models.FloatField(default=0)

    max_valuation = models.IntegerField(default=0)
    min_valuation = models.IntegerField(default=0)

    # created_at = models.DateTimeField(nullable=False, default=timezone.now)
    # updated_at = models.DateTimeField(nullable=False, default=timezone.now, onupdate=timezone.now)

