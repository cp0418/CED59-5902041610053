<?php
namespace backend\models;

use yii\behaviors\BlameableBehavior;
use yii\behaviors\TimestampBehavior;


class Subject extends \common\models\Subject
{
    public function behaviors()
    {
        return [
            //Behavior name 
            TimestampBehavior::class,
            BlameableBehavior::class
        ];
    }
    public function rules(){
        return [
            ['name','required','message'=>'Please fill data'],
            ['name','email','message'=>'Please  fill type email']
        ];
    }



}