package com.example.c_bin;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONObject;

public class Usermakepayment extends AppCompatActivity implements JsonResponse{


    EditText e1,e2,e3,e4,e5;
    Button b1;
    String card,cvv,exp,name,amount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_usermakepayment);
        e1=(EditText)findViewById(R.id.etcard);
        e2=(EditText)findViewById(R.id.etcvv);
        e3=(EditText)findViewById(R.id.etexp);
        e4=(EditText)findViewById(R.id.etname);
        e5=(EditText)findViewById(R.id.etamount);
        e5.setText(Userviewbookedcargo.amounts);
        e5.setEnabled(false);

        b1=(Button)findViewById(R.id.button);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                card=e1.getText().toString();
                cvv=e2.getText().toString();
                exp=e3.getText().toString();
                name=e4.getText().toString();
                amount=e5.getText().toString();

                if (e1.getText().toString().equalsIgnoreCase("")) {
                    Toast.makeText(getApplicationContext(),
                            "Enter All The Fields", Toast.LENGTH_LONG).show();
                    e1.setError("");
                    e1.setFocusable(true);

                } else if (e1.getText().toString().length() != 16) {
                    Toast.makeText(getApplicationContext(), "16 Digit",
                            Toast.LENGTH_LONG).show();
                    e1.setError("");
                    e1.setFocusable(true);

                } else if (e2.getText().toString().equalsIgnoreCase("")) {
                    Toast.makeText(getApplicationContext(),
                            "Enter All The Fields", Toast.LENGTH_LONG).show();
                    e2.setError("");
                    e2.setFocusable(true);

                } else if (e2.getText().toString().length() != 3) {
                    Toast.makeText(getApplicationContext(), "3 Digit",
                            Toast.LENGTH_LONG).show();
                    e2.setError("");
                    e2.setFocusable(true);

                } else if (e3.getText().toString().equalsIgnoreCase("")) {
                    Toast.makeText(getApplicationContext(),
                            "Enter All The Fields", Toast.LENGTH_LONG).show();
                    e3.setError("");
                    e3.setFocusable(true);
                } else if (e4.getText().toString().equalsIgnoreCase("")) {
                    Toast.makeText(getApplicationContext(),
                            "Enter All The Fields", Toast.LENGTH_LONG).show();
                    e4.setError("");
                    e4.setFocusable(true);
                }

                else {

                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) Usermakepayment.this;
                    String q = "/usermakepayment?oid=" + Userviewbookedcargo.oids + "&amount=" + Userviewbookedcargo.amounts;
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }
            }
        });

    }

    @Override
    public void response(JSONObject jo) {
        try {


            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                Toast.makeText(getApplicationContext(), "PAID SUCCESSFULLY", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), Usermakepayment.class));

            } else {

                Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
            }



        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }
}