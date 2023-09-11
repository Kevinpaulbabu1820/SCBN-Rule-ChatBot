1.	Create a cloud function.
2.	Create an openAPI json document.	(Use the link below for how to)
3.	Go to Watson assistant -> Integrations -> Build custom extension
4.	Upload your openAPI json file.
5.	After creating this extension, click Add on it. Review and save.
6.	Now create an action. And go to from whichever node you want to call the cloud function.
7.	In the ‘And then’ section at bottom, select use an extension. Choose appropriate options and set the parameters (using session variables, or text, etc).
8.	Test the action.	(Disable the dialog skill first, worked for me only after that)

https://medium.com/@yi.angela/connecting-watson-assistant-to-db2-with-ibm-cloud-function-and-a-custom-extension-89bbe4c6a83b
