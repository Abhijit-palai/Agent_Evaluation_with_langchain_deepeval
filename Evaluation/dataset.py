from deepeval .dataset import EvaluationDataset , Golden
from deepeval.test_case import ToolCall


# Take Handwritten Golden dataset for evaluating the tool in diff diff conditions.
dataset = EvaluationDataset(
    goldens = [
        Golden(
            input = "I am user123 , I would like a refund for the book and the pen",
            expected_output="A refund ticket for 30$ has been issued successfully",
            expected_tools=[
                ToolCall(name="get_user_purchase_history"),
                ToolCall(name="calculate_right_refund"),
                ToolCall(name="issue_refund_ticket"),
                ToolCall(name="get_today_date")
            ]
        ),
        
        Golden(
                    input = "I am user123 , I would like a refund for the notebook",
                    expected_output="A refund ticket for 23$ has been issued successfully",
                    expected_tools=[
                        ToolCall(name="get_user_purchase_history"),
                        ToolCall(name="calculate_right_refund"),
                        ToolCall(name="issue_refund_ticket"),
                        ToolCall(name="get_today_date")
                    ]
                ),
        Golden(
                            input = "I am user123 , I would like no refund , I just want to what i purchased",
                            expected_output="No refund tickets were issued only a list of what they bought",
                            expected_tools=[
                                ToolCall(name="get_user_purchase_history")                               
                            ]
                        ),
         
        Golden(
                             input = "I am user999 , I would like a refund for the notebook",
                             expected_output="Tell the user that the user name is not valid and ask for username again before giving info about a refund",
                             expected_tools=[
                                 ToolCall(name="get_user_purchase_history")
                             ]
                         ),
          
        Golden(
                              input = "I am user126 , I would like a refund for the water_bottle",
                              expected_output="A refund given because it is outside of the 30 days guideline",
                              expected_tools=[
                                  ToolCall(name="get_user_purchase_history"),
                                  ToolCall(name="get_today_date")
                              ]
                          ),
        Golden(
                               input = "I am user126 , I would like a refund for the backpack and water_bottle",
                               expected_output="A refund ticket for 45$ has been issued successfully only for the backpack. The water_bottle is not eligible for a refund because it is outside 30 days refund policy",
                               expected_tools=[
                                   ToolCall(name="get_user_purchase_history"),
                                   ToolCall(name="calculate_right_refund"),
                                   ToolCall(name="issue_refund_ticket"),
                                   ToolCall(name="get_today_date")
                               ]
                           ),
            
        Golden(
                                           input = "I am user126 , I would like a refund for the sneakers",
                                           expected_output="No refund was given because you didn't purchase this item",
                                           expected_tools=[
                                               ToolCall(name="get_user_purchase_history")
                                           ]
                                       ),
                        
            
    ]
)