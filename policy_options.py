from MathSpecMapping import PolicyActionOption
from messages import InitiateStakingRewardMessage, StakingRewardMessage, VoteForSlashingMessage, SlashingMessage

policy_options = {}

policy_options["Purchase Compute Credits Policy"] = []
policy_options["Stake for License Policy"] = []
policy_options["Increase Stake Policy"] = []
policy_options["Decrease Stake Policy"] = []
policy_options["App API Request Via Ingress Policy"] = []
policy_options["Monitor Performance Send API Request"] = []
policy_options['Monitor Performance Receive API Request'] = []
policy_options["New NFT Creation Policy"] = []
policy_options["Increase Stake Policy (Node Operator)"] = []
policy_options["Buyback for Burn Policy"] = []
policy_options["Earn Staking Rewards Policy"] = [PolicyActionOption(
    label="Placeholder Stake Reward", description="This is a simple function for how earning stake could work",
    inputs=[InitiateStakingRewardMessage],
    outputs=[StakingRewardMessage],
    logic="""
    <br/>1. Check last reward was after PARAMS.min_reward_days, if false terminate
<br/>
2. Pull the delta time from last reward and find yield based on parameters, define it as amount
<br/>
3. Create StakingRewardMessage from the InitiateStakingRewardMessage fields as well as the new field reward_amount = amount
<br/>
4. Call Increase Token Holder Funds and Decrease Treasury Funds both with this message
    """)]
policy_options["Slashing Policy"] = [PolicyActionOption(
    label="Placeholder Slashing", description="This is a simple function for how slashing could work",
    inputs=[VoteForSlashingMessage],
    outputs=[SlashingMessage],
    logic="""
    <br/>1. Check INPUTS[0].details == "SLASH", if not terminate the function
<br/>
2. Find the amount of stake for INPUTS[0].operator in the treasury, define this as slash_amount
<br/>
3. Create a variable o1 = SlashingMessage(...INPUTS[0], slashed_amount=slash_amount)
<br/>
4. Call Decrease Treasury Stake with the o1 message
    """)]
